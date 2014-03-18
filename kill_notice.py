import znc

class kill_notice(znc.Module):
    module_types = [znc.CModInfo.GlobalModule]
    description = "This global module sends a notice to all admins whenever a user is killed off a server."
    wiki_page = "kill_notice"

    def OnRaw(self, line):
        cmd = str(line).split()[0].lower()

        if cmd == "error":
            rest = " ".join(str(line).split()[1:]).lower()

            if "lined" in rest or "killed" in srest:
                rest = " ".join(str(line).split()[1:])
                self.AdminNotify(str(self.GetUser().GetUserName())+" (killed: "+rest+")")

    def AdminNotify(self, msg):
        znc.CZNC.Get().Broadcast(str(msg), True)
