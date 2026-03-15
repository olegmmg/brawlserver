using BSL.v41.Logic.Database.Account;
using BSL.v41.Logic.Environment.LaserNotification.Laser.Own;

namespace BSL.v41.Logic.Environment.LaserNotification;

public class NotificationFactory
{
    public AccountModel AccountModel { get; set; } = null!;
    public Dictionary<int, BaseNotification> FreeTextNotifications { get; set; } = new();
}
