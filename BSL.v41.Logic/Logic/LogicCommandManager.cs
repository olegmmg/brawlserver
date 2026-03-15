using BSL.v41.Logic.Environment.LaserCommand;
using BSL.v41.Titan.DataStream;

namespace BSL.v41.Logic.Logic;

/// <summary>
/// Stub for LogicCommandManager - actual implementation is in BSL.v41.Tools DLL
/// </summary>
public static class LogicCommandManager
{
    private static readonly Dictionary<int, Func<LogicCommand>> CommandFactories = new()
    {
        // Client commands
        { 500, () => new LogicCommand() },
        { 501, () => new LogicCommand() },
        { 502, () => new LogicCommand() },
        { 503, () => new LogicCommand() },
    };

    public static LogicCommand? DecodeCommand(ByteStream byteStream)
    {
        try
        {
            var commandId = byteStream.ReadVInt();
            var command = CommandFactories.TryGetValue(commandId, out var factory)
                ? factory()
                : new LogicCommand();
            command.Decode(byteStream);
            return command;
        }
        catch
        {
            return null;
        }
    }

    public static void EncodeCommand(LogicCommand command, ByteStream byteStream)
    {
        try
        {
            command.Encode(byteStream);
        }
        catch { /* ignore */ }
    }
}
