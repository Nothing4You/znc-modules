import znc

class kill_notice(znc.Module):
    module_types = [znc.CModInfo.GlobalModule]
    description = "Example python3 module for ZNC"

    def OnRaw(self, line):
        cmd = str(line).split()[0].lower()

        if cmd == "error":
            rest = " ".join(str(line).split()[1:]).lower()

            if "lined" in rest or "killed" in srest:
                rest = " ".join(str(line).split()[1:])
                self.AdminNotify(str(self.GetUser().GetUserName())+" (killed: "+rest+")")

    def AdminNotify(self, msg):
        znc.CZNC.Get().Broadcast(str(msg), True)
