import subprocess
from ..provider import Provider
from ..pager import paged_subprocess

CMD_INSTALL = ['apt', 'install']
CMD_REMOVE = ['apt', 'remove']
CMD_UPGRADE = ['apt', '-y', 'upgrade']
CMD_UPDATE = ['apt', '-y', 'update']
CMD_SEARCH = ['apt', 'search']
CMD_INFO = ['apt', 'show']
CMD_CLEAN = ['apt', 'autoclean']
CMD_CLEAN_DEEP = ['apt', 'clean']
CMD_INSTALLED = ['dpkg-query', '--show', '-f', '${Package}\n']

class AptProvider(Provider):
    
    def install(self, *package:str) -> bool:
        return subprocess.Popen([*CMD_INSTALL, *package]).wait() == 0
        
    def remove(self, *package:str) -> bool:
        """remove a package or a series of packages"""
        return subprocess.Popen([*CMD_REMOVE, *package]).wait() == 0
    
    def upgrade(self) -> bool:
        return subprocess.Popen(CMD_UPGRADE).wait() == 0
    
    def update(self) -> bool:
        return subprocess.Popen(CMD_UPDATE).wait() == 0
    
    def search(self, query:str) -> bool:
        return paged_subprocess([*CMD_SEARCH, query]).wait() == 0
        
    def info(self, package:str) -> bool:
        return subprocess.Popen([*CMD_INFO, package]).wait() == 0
    
    def stats(self) -> bool:
        raise NotImplemented()
    
    def clean(self, deep:bool=False) -> bool:
        return subprocess.Popen(CMD_CLEAN_DEEP if deep else CMD_CLEAN).wait() == 0
    
    def list_installed(self) -> bool:
        return subprocess.Popen(CMD_INSTALLED).wait() == 0
    
    
