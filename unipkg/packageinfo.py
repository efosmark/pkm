from dataclasses import dataclass

def ellipsis(text:str|None, maxlen:int) -> str:
    if text is None:
        text = ''
    if len(text) > maxlen:
        text = f'{text[:maxlen-1]}…'
    return f'{text: <{maxlen}}'

@dataclass
class PackageInfo:
    repo:str|None = ''
    name:str|None = ''
    version:str|None = ''
    size:str|None = ''
    notes:list|None = None
    metapackage:str|None = None
    description:str|None = ''
    
    def __str__(self):
        return ' '.join([
            ellipsis(self.repo, 5),
            ellipsis(self.name, 35),
            ellipsis(self.version, 10),
            self.description or ''
        ])