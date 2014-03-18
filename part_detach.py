import znc

class part_detach(znc.Module):
    module_types = [znc.CModInfo.NetworkModule]
    description = "Client parting is converted in detaching the channel"
    wiki_page = "part_detach"

    def OnUserPart(self, channel, message):
        chan = self.GetNetwork().FindChan(channel.s)
        
        if not chan.IsDetached() and chan.InConfig():
            chan.DetachUser()
            return znc.HALTCORE

        return znc.CONTINUE
