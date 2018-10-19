from ._wx_CommandEvent import CommandEvent
from ._wx_Origin import Origin

class HelpEvent(CommandEvent):
    Origin_Unknown: Origin
    Origin_Keyboard: Origin
    Origin_HelpButton: Origin
