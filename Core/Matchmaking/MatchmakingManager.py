import time
import threading
from Utils.Helpers import Helpers

_ = print

# Matchmaking queue: list of {"client": ..., "player": ..., "joined_at": float, "map_id": int, "mode": str}
_queue = []
_queue_lock = threading.Lock()
_timer_thread = None
_timer_started = False

WAIT_TIME = 10  # seconds
MAX_PLAYERS = 6  # 3v3


def _get_mode(map_id):
    """Determine if it's showdown (solo/duo) or 3v3 based on map_id.
    For simplicity all modes are treated as 3v3 here."""
    return "3v3"


def _fill_with_bots(players, total):
    """Return list of bot slot dicts to fill up to total slots."""
    bots = []
    needed = total - len(players)
    for i in range(needed):
        bots.append({"is_bot": True, "bot_id": i + 1})
    return bots


def _launch_game(players):
    """Send battle start packets to all real players."""
    from Protocol.Messages.Server.TeamMessage import TeamMessage
    from Protocol.Messages.Server.MatchMakingCancelledMessage import MatchMakingCancelledMessage

    real = [p for p in players if not p.get("is_bot")]
    bot_count = len([p for p in players if p.get("is_bot")])

    _( f"{Helpers.green}[Matchmaking] Launching game: {len(real)} players + {bot_count} bots")

    for entry in real:
        try:
            TeamMessage(entry["client"], entry["player"]).send()
        except Exception as e:
            _(f"{Helpers.red}[Matchmaking] Error sending TeamMessage: {e}")


def _assign_teams(player_entries):
    """
    Build teams based on player count (3v3 mode):
    - 6 players  → 3v3, no bots
    - 4-5 players → team1 = players[:3], team2 = rest + bots
    - 2-3 players → team1 = players[:min(3)], team2 = all bots (up to 3)
    - 1 player   → wait more / fill with bots

    Returns list of all slots (real + bot) ready to launch.
    """
    count = len(player_entries)
    total = MAX_PLAYERS

    if count >= total:
        # Full lobby
        return player_entries[:total]
    elif count >= 4:
        # 1 team full of players, other team gets bots to fill
        bots = _fill_with_bots(player_entries, total)
        return player_entries + bots
    elif count >= 2:
        # 2+ players: fill rest with bots
        bots = _fill_with_bots(player_entries, total)
        return player_entries + bots
    else:
        # Only 1 player — still launch with bots
        bots = _fill_with_bots(player_entries, total)
        return player_entries + bots


def _matchmaking_loop():
    global _timer_started
    while True:
        time.sleep(1)
        with _queue_lock:
            if not _queue:
                _timer_started = False
                continue

            oldest = _queue[0]["joined_at"]
            elapsed = time.time() - oldest

            count = len(_queue)
            _(f"{Helpers.cyan}[Matchmaking] Queue: {count} players, elapsed: {elapsed:.1f}s")

            # Launch immediately if full lobby
            if count >= MAX_PLAYERS:
                players = list(_queue[:MAX_PLAYERS])
                del _queue[:MAX_PLAYERS]
                _timer_started = False
                threading.Thread(target=_launch_game, args=(_assign_teams(players),), daemon=True).start()

            # Launch after 10s with whatever we have (min 2 players)
            elif elapsed >= WAIT_TIME and count >= 2:
                players = list(_queue)
                _queue.clear()
                _timer_started = False
                threading.Thread(target=_launch_game, args=(_assign_teams(players),), daemon=True).start()

            # After 10s with only 1 player — launch solo + bots
            elif elapsed >= WAIT_TIME and count == 1:
                players = list(_queue)
                _queue.clear()
                _timer_started = False
                threading.Thread(target=_launch_game, args=(_assign_teams(players),), daemon=True).start()


def start_loop():
    t = threading.Thread(target=_matchmaking_loop, daemon=True)
    t.start()


def enqueue(client, player):
    """Add player to matchmaking queue."""
    global _timer_started
    with _queue_lock:
        # Don't add duplicates
        for entry in _queue:
            if entry["player"].ID == player.ID:
                return

        _queue.append({
            "client": client,
            "player": player,
            "joined_at": time.time(),
        })
        _( f"{Helpers.green}[Matchmaking] Player {player.name} joined queue. Total: {len(_queue)}")


def dequeue(player_id):
    """Remove player from queue (e.g. cancel matchmaking)."""
    with _queue_lock:
        global _queue
        before = len(_queue)
        _queue = [e for e in _queue if e["player"].ID != player_id]
        if len(_queue) < before:
            _(f"{Helpers.yellow}[Matchmaking] Player {player_id} left queue.")
