from typing import overload
class Size:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__ (self, width: int, height: int) -> None: ...

DefaultSize: Size
