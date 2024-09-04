from typing import Sequence

class TinyScanner:
    WS = ['\n', '\t', ' ']
    
    def __init__(self, data:Sequence):
        self.data = data
        self.idx = 0
    
    def curr(self) -> str|None:
        try:
            return self.data[self.idx]
        except IndexError:
            return None
    
    def read(self) -> str|None:
        ch = self.curr()
        if ch is not None:
            self.idx += 1
        return ch
    
    def expect(self, char:str, ignore_ws:bool=True) -> bool:
        while ignore_ws and self.curr() in self.WS and self.curr() != char:
            self.read()
        if self.curr() == char:
            self.read()
            return True
        return False
    
    def read_until(self, expected:str|None=None, *, ignore_ws:bool=True, keep_expected:bool=False) -> str|None:
        while ignore_ws and self.curr() in self.WS and self.curr() != expected:
            self.read()
        values = []
        while self.curr() is not None:
            ch = self.read()
            if ch == expected:
                if keep_expected:
                    values.append(ch)
                break
            values.append(ch)
        if len(values) == 0:
            return None
        return ''.join(values)
