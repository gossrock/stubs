from ._wx_EvtHandler import EvtHandler
class WindowBase(EvtHandler):
    def  AddChild(self, child: WindowBase) -> None: ...
    def RemoveChild(self, child: WindowBase) -> None: ...
