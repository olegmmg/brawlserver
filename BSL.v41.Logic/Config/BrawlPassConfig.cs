using Newtonsoft.Json;

namespace BSL.v41.Logic.Config;

// Reward types used in brawlpass.json
public enum BpRewardType { Box, BigBox, MegaBox, Gems, Gold, PowerPoints, Skin, Brawler, Pin, PinPack }

public class BpReward
{
    [JsonProperty("tier")]    public int Tier   { get; set; }
    [JsonProperty("type")]    public string Type { get; set; } = "";
    [JsonProperty("amount")]  public int Amount  { get; set; }
    [JsonProperty("skin_id")] public int SkinId  { get; set; }
    [JsonProperty("brawler_id")] public int BrawlerId { get; set; }
    [JsonProperty("pin_id")]  public int PinId   { get; set; }
    [JsonProperty("name")]    public string Name  { get; set; } = "";

    public BpRewardType RewardType => Enum.Parse<BpRewardType>(Type, ignoreCase: true);
}

public class BrawlPassConfig
{
    [JsonProperty("season_id")]            public int SeasonId           { get; set; } = 9;
    [JsonProperty("pass_price_gems")]      public int PassPriceGems      { get; set; } = 169;
    [JsonProperty("pass_plus_price_gems")] public int PassPlusPriceGems  { get; set; } = 249;
    [JsonProperty("pass_plus_bonus_tiers")]public int PassPlusBonusTiers { get; set; } = 8;
    [JsonProperty("end_time_days")]        public int EndTimeDays         { get; set; } = 70;
    [JsonProperty("post_pass_xp_per_big_box")] public int PostPassXpPerBigBox { get; set; } = 500;
    [JsonProperty("free_rewards")]         public List<BpReward> FreeRewards { get; set; } = [];
    [JsonProperty("paid_rewards")]         public List<BpReward> PaidRewards { get; set; } = [];

    // Singleton with hot-reload via FileSystemWatcher
    private static BrawlPassConfig? _instance;
    private static FileSystemWatcher? _watcher;
    private static readonly object Lock = new();

    public static BrawlPassConfig Instance
    {
        get
        {
            if (_instance != null) return _instance;
            lock (Lock) { _instance ??= Load(); }
            return _instance;
        }
    }

    public static void StartWatcher(string path = "brawlpass.json")
    {
        var dir  = Path.GetDirectoryName(Path.GetFullPath(path)) ?? ".";
        var file = Path.GetFileName(path);
        _watcher = new FileSystemWatcher(dir, file)
        {
            NotifyFilter = NotifyFilters.LastWrite,
            EnableRaisingEvents = true
        };
        _watcher.Changed += (_, _) =>
        {
            Thread.Sleep(300); // wait for file to be fully written
            lock (Lock)
            {
                _instance = Load(path);
                Console.WriteLine("[BrawlPass] Config reloaded from disk.");
            }
        };
        Console.WriteLine($"[BrawlPass] Watching {path} for changes...");
    }

    private static BrawlPassConfig Load(string path = "brawlpass.json")
    {
        try
        {
            var json = File.ReadAllText(path);
            return JsonConvert.DeserializeObject<BrawlPassConfig>(json) ?? new BrawlPassConfig();
        }
        catch (Exception e)
        {
            Console.WriteLine($"[BrawlPass] Failed to load config: {e.Message}");
            return new BrawlPassConfig();
        }
    }
}
