from typing import List, Optional

from ._wx_AppConsole import AppConsole

from ._wx_Window import Window

from ._wx_VideoMode import VideoMode
from ._wx_AppAssertMode import AppAssertMode
from ._wx_LayoutDirection import LayoutDirection as wx_LayoutDirection

class PyApp(AppConsole):
    AssertMode: AppAssertMode
    DisplayMode: VideoMode
    ExitOnFrameDelete: bool
    LayoutDirection: wx_LayoutDirection
    TopWindow: Window
    UseBestVisual: bool

    def  GetAssertMode(self) -> AppAssertMode: ...
    @staticmethod
    def GetComCtl32Version() -> int: ...
    def GetDisplayMode(self) -> VideoMode: ...
    def GetExitOnFrameDelete(self) -> bool: ...
    def GetLayoutDirection(self) -> wx_LayoutDirection: ...
    @staticmethod
    def GetShell32Version() -> int: ...
    def GetTopWindow(self) -> Window: ...
    def GetUseBestVisual(self) -> bool: ...
    def IsActive(self) -> bool: ...
    @staticmethod
    def IsDisplayAvailable() -> bool: ...
    def MacHideApp(self) -> None: ...
    def MacNewFile(self) -> None: ...
    def MacOpenFile(self, fileName: str) -> None: ... #depricated
    def MacOpenFiles(self, fileNames: List[str]) -> None: ...
    def MacOpenURL(self, url: str) -> None: ...
    def MacPrintFile(self, fileName: str) -> None: ...
    def MacReopenApp(self) -> None: ...
    def OSXIsGUIApplication(self) -> bool: ...
    def SafeYield(self, win: Window, onlyIfNeeded: bool) -> bool: ...
    def SafeYieldFor(self, win: Window, eventsToProcess: int) -> bool: ...
    def SetAssertMode(self, AppAssertMode: AppAssertMode) -> None: ...
    def SetDisplayMode(self, info: VideoMode) -> bool: ...
    def SetExitOnFrameDelete(self, flag: bool) -> None: ...
    def SetNativeTheme(self, theme: str) -> bool: ...
    def SetTopWindow(self, window: Optional[Window]) -> None: ...
    def SetUseBestVisual(self, flag: bool, forceTrueColour: bool = False) -> None: ...