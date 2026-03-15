using BSL.v41.Logic.Config;
using BSL.v41.Titan.Graphic;

namespace BSL.v41.General;

public static class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine(@"
    ____               _           __     __  ___                       __ 
   / __ \_________    (_)__  _____/ /_   /  |/  /___ _____ _____  ___  / /_
  / /_/ / ___/ __ \  / / _ \/ ___/ __/  / /|_/ / __ `/ __ `/ __ \/ _ \/ __/
 / ____/ /  / /_/ / / /  __/ /__/ /_   / /  / / /_/ / /_/ / / / /  __/ /_  
/_/   /_/   \____/_/ /\___/\___/\__/  /_/  /_/\__,_/\__, /_/ /_/\___/\__/  
                /___/                               /____/                   
");
        ConsoleLogger.WriteTextWithPrefix(ConsoleLogger.Prefixes.Cmd, "Project_Magnet starting...");

        // Start hot-reload watchers for configs
        BrawlPassConfig.StartWatcher("brawlpass.json");
        ShopConfig.StartWatcher("shop.json");
        ConsoleLogger.WriteTextWithPrefix(ConsoleLogger.Prefixes.Cmd,
            $"BrawlPass season {BrawlPassConfig.Instance.SeasonId} loaded. " +
            $"Pass: {BrawlPassConfig.Instance.PassPriceGems} gems, " +
            $"Pass+: {BrawlPassConfig.Instance.PassPlusPriceGems} gems.");
        ConsoleLogger.WriteTextWithPrefix(ConsoleLogger.Prefixes.Cmd,
            $"Shop loaded: {ShopConfig.Data.Offers.Count} offers.");

        // Telegram Bot
        var telegramToken = Environment.GetEnvironmentVariable("TELEGRAM_TOKEN");
        var adminId = Environment.GetEnvironmentVariable("ADMIN_ID");
        if (!string.IsNullOrEmpty(telegramToken))
        {
            ConsoleLogger.WriteTextWithPrefix(ConsoleLogger.Prefixes.Cmd, "Starting Telegram bot...");
            Task.Run(() => TelegramBot.Start(telegramToken, adminId));
        }
    }
}
