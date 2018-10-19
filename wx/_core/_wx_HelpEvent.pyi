from . import CommandEvent
from . import Origin

class HelpEvent(CommandEvent):
    Origin_Unknown: Origin
    Origin_Keyboard: Origin
    Origin_HelpButton: Origin
