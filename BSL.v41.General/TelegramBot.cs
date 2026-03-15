using BSL.v41.Logic.Environment.LaserMessage.Sepo.Home.Laser.Laser;
using BSL.v41.Titan.Graphic;
using System.Net.Http;
using System.Text;
using System.Text.Json;

namespace BSL.v41.General;

public static class TelegramBot
{
    private static string _token = "";
    private static string? _adminId;
    private static long _lastUpdateId = 0;
    private static readonly HttpClient Http = new();
    private static readonly DateTime StartTime = DateTime.UtcNow;

    public static void Start(string token, string? adminId)
    {
        _token = token;
        _adminId = adminId;
        ConsoleLogger.WriteTextWithPrefix(ConsoleLogger.Prefixes.Cmd, "Telegram bot started!");

        if (!string.IsNullOrEmpty(_adminId))
            SendMessage(_adminId,
                "✅ *Project\\_Magnet* запущен\\!\n" +
                "/status \\- статус сервера\n" +
                "/players \\- онлайн игроков\n" +
                "/reload \\- перезагрузить конфиги");

        while (true)
        {
            try { Poll(); }
            catch (Exception e)
            {
                ConsoleLogger.WriteTextWithPrefix(ConsoleLogger.Prefixes.Cmd, $"Telegram error: {e.Message}");
            }
            Thread.Sleep(2000);
        }
    }

    private static void Poll()
    {
        var url = $"https://api.telegram.org/bot{_token}/getUpdates?offset={_lastUpdateId + 1}&timeout=10";
        var resp = Http.GetStringAsync(url).Result;
        var doc = JsonDocument.Parse(resp);
        var updates = doc.RootElement.GetProperty("result");

        foreach (var update in updates.EnumerateArray())
        {
            _lastUpdateId = update.GetProperty("update_id").GetInt64();
            if (!update.TryGetProperty("message", out var msg)) continue;

            var chatId = msg.GetProperty("chat").GetProperty("id").ToString();
            var text = msg.TryGetProperty("text", out var t) ? t.GetString() ?? "" : "";

            if (_adminId != null && chatId != _adminId) continue;

            switch (text.ToLower().Trim())
            {
                case "/status":
                    var uptime = DateTime.UtcNow - StartTime;
                    SendMessage(chatId,
                        $"🟢 Project\\_Magnet Online\n" +
                        $"⏱ Uptime: {(int)uptime.TotalHours}h {uptime.Minutes}m\n" +
                        $"👥 Players: {GetPlayerCount()}\n" +
                        $"🎯 BP Season: {BrawlPassConfig.Instance.SeasonId}");
                    break;

                case "/players":
                    SendMessage(chatId, $"👥 Online: {GetPlayerCount()} players");
                    break;

                case "/reload":
                    // Force reload both configs
                    try
                    {
                        BrawlPassConfig.StartWatcher("brawlpass.json");
                        ShopConfig.StartWatcher("shop.json");
                        SendMessage(chatId,
                            $"✅ Конфиги перезагружены\\!\n" +
                            $"BP season: {BrawlPassConfig.Instance.SeasonId}\n" +
                            $"Shop offers: {ShopConfig.Data.Offers.Count}");
                    }
                    catch (Exception e)
                    {
                        SendMessage(chatId, $"❌ Ошибка: {e.Message}");
                    }
                    break;

                default:
                    SendMessage(chatId,
                        "Команды:\n" +
                        "/status \\- статус\n" +
                        "/players \\- онлайн\n" +
                        "/reload \\- перезагрузить конфиги");
                    break;
            }
        }
    }

    private static void SendMessage(string chatId, string text)
    {
        try
        {
            var url = $"https://api.telegram.org/bot{_token}/sendMessage";
            var payload = JsonSerializer.Serialize(new
            {
                chat_id = chatId,
                text,
                parse_mode = "MarkdownV2"
            });
            Http.PostAsync(url, new StringContent(payload, Encoding.UTF8, "application/json")).Wait();
        }
        catch { /* ignore send errors */ }
    }

    private static int GetPlayerCount()
    {
        try
        {
            return BSL.v41.Logic.Environment.LaserListener.IdentifierListener
                .GetLogicGameListeners().Count;
        }
        catch { return 0; }
    }
}
