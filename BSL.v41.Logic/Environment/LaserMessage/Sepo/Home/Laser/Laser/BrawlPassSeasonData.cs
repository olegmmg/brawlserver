using BSL.v41.Logic.Database.Account;
using BSL.v41.Titan.DataStream;
using BSL.v41.Titan.Utilities;

namespace BSL.v41.Logic.Environment.LaserMessage.Sepo.Home.Laser.Laser;

public class BrawlPassSeasonData(AccountModel accountModel)
{
    // Item type IDs used by BS v41 protocol
    // These are ShopItemHelperTable enum values:
    // 0=Box, 1=BigBox, 2=MegaBox, 3=Gems, 4=Gold/Coins, 5=PowerPoints, 6=Skin, 8=Pin
    private static readonly Dictionary<BpRewardType, int> TypeIds = new()
    {
        { BpRewardType.Box,         0 },
        { BpRewardType.BigBox,      1 },
        { BpRewardType.MegaBox,     2 },
        { BpRewardType.Gems,        3 },
        { BpRewardType.Gold,        4 },
        { BpRewardType.PowerPoints, 5 },
        { BpRewardType.Skin,        6 },
        { BpRewardType.Brawler,     7 },
        { BpRewardType.Pin,         8 },
        { BpRewardType.PinPack,     9 },
    };

    public void Encode(ByteStream byteStream)
    {
        var cfg = BrawlPassConfig.Instance;

        // Determine if this player has BrawlPass
        // For now: everyone gets free pass (can be tied to accountModel later)
        var hasPass     = true;
        var hasPassPlus = false; // set true if player bought +8 tiers

        // Season info
        byteStream.WriteVInt(cfg.SeasonId);          // season_id
        byteStream.WriteVInt(0);                      // current XP (player's BP progress)
        byteStream.WriteBoolean(hasPass || hasPassPlus); // has_pass
        byteStream.WriteVInt(hasPassPlus ? cfg.PassPlusBonusTiers : 0); // bonus tiers from pass+

        // Free rewards track (71 tiers: 0-70)
        byteStream.WriteByte(2); // marker
        var freeDict = cfg.FreeRewards.ToDictionary(r => r.Tier);
        for (var i = 0; i <= 70; i++)
        {
            if (freeDict.TryGetValue(i, out var reward))
            {
                byteStream.WriteInt(TypeIds.GetValueOrDefault(reward.RewardType, 0));
                byteStream.WriteInt(reward.Amount > 0 ? reward.Amount : 1);
                byteStream.WriteInt(reward.SkinId > 0 ? reward.SkinId : 
                                    reward.BrawlerId > 0 ? reward.BrawlerId :
                                    reward.PinId > 0 ? reward.PinId : 0);
                byteStream.WriteInt(0); // claimed flag (0 = not claimed)
            }
            else
            {
                byteStream.WriteInt(0);
                byteStream.WriteInt(0);
                byteStream.WriteInt(0);
                byteStream.WriteInt(0);
            }
        }

        // Paid rewards track (71 tiers: 0-70)
        byteStream.WriteByte(1); // marker
        var paidDict = cfg.PaidRewards.ToDictionary(r => r.Tier);
        for (var i = 0; i <= 70; i++)
        {
            if (paidDict.TryGetValue(i, out var reward))
            {
                byteStream.WriteInt(TypeIds.GetValueOrDefault(reward.RewardType, 0));
                byteStream.WriteInt(reward.Amount > 0 ? reward.Amount : 1);
                byteStream.WriteInt(reward.SkinId > 0 ? reward.SkinId :
                                    reward.BrawlerId > 0 ? reward.BrawlerId :
                                    reward.PinId > 0 ? reward.PinId : 0);
                byteStream.WriteInt(0); // claimed flag
            }
            else
            {
                byteStream.WriteInt(0);
                byteStream.WriteInt(0);
                byteStream.WriteInt(0);
                byteStream.WriteInt(0);
            }
        }

        // End time (seconds from now)
        var endSeconds = cfg.EndTimeDays * 24 * 3600;
        byteStream.WriteInt(endSeconds);

        // Pass prices
        byteStream.WriteInt(cfg.PassPriceGems);
        byteStream.WriteInt(cfg.PassPlusPriceGems);
    }
}
