class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = 'mirror'
        self.UnzipMirrorCommand = 'unzipmirror'
        self.TarMirrorCommand = 'tarmirror'
        self.CancelMirror = 'cancel'
        self.CancelAllCommand = 'cancelall'
        self.ListCommand = 'list'
        self.deleteCommand = 'del'
        self.StatusCommand = 'status'
        self.AuthorizedUsersCommand = 'users'
        self.AuthorizeCommand = 'auth'
        self.UnAuthorizeCommand = 'unauth'
        self.AddSudoCommand = 'addsudo'
        self.RmSudoCommand = 'rmsudo'
        self.PingCommand = 'ping'
        self.RestartCommand = 'restart'
        self.StatsCommand = 'stats'
        self.HelpCommand = 'help'
        self.LogCommand = 'log'
        self.CloneCommand = "clone"
        self.WatchCommand = 'watch'
        self.TarWatchCommand = 'tarwatch'

BotCommands = _BotCommands()
