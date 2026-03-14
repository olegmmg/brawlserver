import time
import threading
from Utils.Helpers import Helpers

_ = print

# Map IDs from Events.json
SOLO_SHOWDOWN_MAPS = {204, 8, 24, 46}
DUO_SHOWDOWN_MAPS  = {45, 57, 97, 1}

SOLO_MAX  = 10
DUO_MAX   = 10
WAIT_TIME = 10  # seconds

_solo_queue = []
_duo_queue  = []
_lock = threading.Lock()

def _mode_for(map_id):
    return "duo" if map_id in DUO_SHOWDOWN_MAPS else "solo"

def _make_bot(i):
    return {"is_bot": True, "bot_index": i}

def _launch(players, max_players, label):
    from Protocol.Messages.Server.TeamMessage import TeamMessage
    real   = [p for p in players if not p.get("is_bot")]
    n_bots = max_players - len(real)
    _(f"{Helpers.green}[Matchmaking][{label}] START: {len(real)} players + {n_bots} bots")
    for entry in real:
        try:
            TeamMessage(entry["client"], entry["player"]).send()
        except Exception as e:
            _(f"{Helpers.red}[Matchmaking][{label}] Error: {e}")

def _tick(queue, max_players, label):
    if not queue:
        return
    elapsed = time.time() - queue[0]["joined_at"]
    count   = len(queue)
    _(f"{Helpers.cyan}[Matchmaking][{label}] {count}/{max_players} players, {elapsed:.1f}s elapsed")
    if count >= max_players:
        players = list(queue[:max_players])
        del queue[:max_players]
        threading.Thread(target=_launch, args=(players, max_players, label), daemon=True).start()
    elif elapsed >= WAIT_TIME:
        players = list(queue)
        queue.clear()
        threading.Thread(target=_launch, args=(players, max_players, label), daemon=True).start()

def _loop():
    while True:
        time.sleep(1)
        with _lock:
            _tick(_solo_queue, SOLO_MAX, "Solo")
            _tick(_duo_queue,  DUO_MAX,  "Duo ")

def start_loop():
    threading.Thread(target=_loop, daemon=True).start()
    _(f"{Helpers.green}[Matchmaking] Started (Solo 10x1 | Duo 5x2 | wait={WAIT_TIME}s)")

def enqueue(client, player):
    mode = _mode_for(player.map_id)
    with _lock:
        queue = _duo_queue if mode == "duo" else _solo_queue
        for e in queue:
            if e["player"].ID == player.ID:
                return
        queue.append({"client": client, "player": player, "joined_at": time.time()})
        _(f"{Helpers.green}[Matchmaking][{mode}] {player.name} joined. Total: {len(queue)}")

def dequeue(player_id):
    with _lock:
        for queue, label in ((_solo_queue, "Solo"), (_duo_queue, "Duo")):
            before = len(queue)
            queue[:] = [e for e in queue if e["player"].ID != player_id]
            if len(queue) < before:
                _(f"{Helpers.yellow}[Matchmaking][{label}] Player {player_id} left.")
                return
