from typing import Callable, Optional

from ._wx_Object import Object
from ._wx_Trackable import Trackable

from ._wx_EventFilter import EventFilter
from ._wx_Event import Event
from .core._wx_PyEventBinder import PyEventBinder

class EvtHandler(Object, Trackable):
    @staticmethod
    def AddFilter(filter: EventFilter) -> None: ...
    def AddPendingEvent(self, event: Event) -> None: ...

    def Bind(self,  event: PyEventBinder,
                    handler: Callable,
                    source:Optional[Object] = None,
                    id: int = -1,
                    id2: int = -1) -> None: ...
