using Newtonsoft.Json;

namespace BSL.v41.Logic.Environment.LaserMessage.Sepo.Home.Laser.Laser;

public class ShopItem
{
    [JsonProperty("type")]    public string Type   { get; set; } = "";
    [JsonProperty("amount")]  public int Amount    { get; set; }
    [JsonProperty("skin_id")] public int SkinId    { get; set; }
}

public class ShopOffer
{
    [JsonProperty("title")]            public string Title           { get; set; } = "";
    [JsonProperty("background")]       public string Background      { get; set; } = "default";
    [JsonProperty("price_type")]       public string PriceType       { get; set; } = "Gems";
    [JsonProperty("price")]            public int Price              { get; set; }
    [JsonProperty("old_price")]        public int OldPrice           { get; set; }
    [JsonProperty("is_daily")]         public bool IsDaily           { get; set; }
    [JsonProperty("confirm_purchase")] public bool ConfirmPurchase   { get; set; }
    [JsonProperty("items")]            public List<ShopItem> Items   { get; set; } = [];
}

public class ShopConfigData
{
    [JsonProperty("offers")] public List<ShopOffer> Offers { get; set; } = [];
}

public static class ShopConfig
{
    private static ShopConfigData? _data;
    private static FileSystemWatcher? _watcher;
    private static readonly object Lock = new();

    public static ShopConfigData Data
    {
        get
        {
            if (_data != null) return _data;
            lock (Lock) { _data ??= Load(); }
            return _data;
        }
    }

    public static void StartWatcher(string path = "shop.json")
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
            Thread.Sleep(300);
            lock (Lock)
            {
                _data = Load(path);
                Console.WriteLine("[Shop] Config reloaded from disk.");
            }
        };
        Console.WriteLine($"[Shop] Watching {path} for changes...");
    }

    private static ShopConfigData Load(string path = "shop.json")
    {
        try
        {
            var json = File.ReadAllText(path);
            return JsonConvert.DeserializeObject<ShopConfigData>(json) ?? new ShopConfigData();
        }
        catch (Exception e)
        {
            Console.WriteLine($"[Shop] Failed to load config: {e.Message}");
            return new ShopConfigData();
        }
    }
}
