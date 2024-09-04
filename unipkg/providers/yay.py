import subprocess
from ..tinyscanner import TinyScanner
from ..provider import Provider
from ..packageinfo import PackageInfo 
from ..pager import paged_subprocess

CMD_INSTALL = ['yay', '-Sy', '--cleanafter', '--removemake', '--answerdiff', 'None', '--answeredit', 'None', '--answerupgrade', 'None']
CMD_REMOVE = ['yay', '-Rns']
CMD_UPGRADE = ['yay', '-Syu', '--cleanafter', '--removemake', '--answerdiff', 'None', '--answeredit', 'None', '--answerupgrade', 'None']
CMD_UPDATE = ['yay -Syu']
CMD_SEARCH = ['yay', '-Ss', '--singlelineresults']
CMD_INFO = ['yay', '-Si']
CMD_CLEAN = ['yay', '-Yc']
CMD_CLEAN_DEEP = ['yay', '-Sc']
CMD_STATS = ['yay', '-Ps']
CMD_INSTALLED = ['yay', '-Qqe']


def _parse_search_line(raw_line:str):
    sc = TinyScanner(raw_line)
    
    r = PackageInfo()
    r.repo = sc.read_until('/')
    r.name = sc.read_until(' ')
    r.version = sc.read_until(' ')
    if sc.expect('('):
        r.size = sc.read_until(')')
    if sc.expect('['):
        r.metapackage = sc.read_until(']')
    while sc.expect('('):
        v = sc.read_until(')')
        if r.notes is None:
            r.notes = []
        r.notes.append(v)
    r.description = sc.read_until()
    return str(r)

class YayProvider(Provider):
    
    def install(self, *package:str) -> bool:
        return subprocess.Popen([*CMD_INSTALL, *package]).wait() == 0
        
    def remove(self, *package:str) -> bool:
        return subprocess.Popen([*CMD_REMOVE, *package]).wait() == 0
    
    def upgrade(self) -> bool:
        return subprocess.Popen(CMD_UPGRADE).wait() == 0
    
    def update(self) -> bool:
        return subprocess.Popen(CMD_UPDATE).wait() == 0
    
    def search(self, query:str) -> bool:
        return paged_subprocess([*CMD_SEARCH, query], modify_line=_parse_search_line).wait() == 0
        
    def info(self, package:str) -> bool:
        return subprocess.Popen([*CMD_INFO, package]).wait() == 0
    
    def stats(self) -> bool:
        return subprocess.Popen(CMD_STATS).wait() == 0
    
    def clean(self) -> bool:
        return subprocess.Popen(CMD_CLEAN).wait() == 0
    
    def list_installed(self) -> bool:
        return subprocess.Popen(CMD_INSTALLED).wait() == 0
    
    
