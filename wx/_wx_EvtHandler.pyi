from typing import Callable, Optional

from ._wx_Object import Object
from ._wx_Trackable import Trackable
from ._wx_EventFilter import EventFilter
from ._wx_Event import Event
from .core._wx_PyEventBinder import PyEventBinder
from . import wxEVT_NULL


class EvtHandler(Object, Trackable):
    EvtHandlerEnabled: bool
    NextHandler: EvtHandler
    PreviousHandler: EvtHandler
    @staticmethod
    def AddFilter(filter: EventFilter) -> None: ...
    def AddPendingEvent(self, event: Event) -> None: ...

    def Bind(self,  event: PyEventBinder, handler: Callable,
                    source:Optional[Object] = None,
                    id: int = -1, id2: int = -1) -> None: ...
    def Connect(self, id: int, lastId: int, eventType: PyEventBinder, func: Callable) -> None: ...
    def DeletePendingEvents(self) -> None: ...
    def Disconnect(self, id: int, lastId: int = -1, eventType: int = wxEVT_NULL, func: Optional[Callable] = None) -> bool: ...
    def GetEvtHandlerEnabled(self) -> bool: ...
    def GetNextHandler(self) -> EvtHandler: ...
    def GetPreviousHandler(self) -> EvtHandler: ...
    def IsUnlinked(self) -> bool: ...
    def ProcessEvent(self, event: Event) -> bool: ...
    def ProcessEventLocally(self, event: Event) -> bool: ...
    def ProcessPendingEvents(self) -> None: ...
    def QueueEvent(self, event: Event) -> None: ...
    @staticmethod
    def RemoveFilter(filter: EventFilter) -> None: ...
    def SafelyProcessEvent(self, event: Event) -> bool: ...
    def SetEvtHandlerEnabled(self, enabled: bool) -> None: ...
    def SetNextHandler(self, handler: EvtHandler) -> None: ...
    def SetPreviousHandler(self, handler: EvtHandler) -> None: ...
    def TryAfter(self, event: Event) -> bool: ...
    def TryBefore(self, event: Event) -> bool: ...
    def Unbind(self, event: PyEventBinder, source: Optional[Object] = None,
                    id: int = ..., id2: int = ...,
                    handler: Optional[Callable] = None) -> bool: ... # sparce documentation, using Bind signature
    def Unlink(self) -> None: ...
