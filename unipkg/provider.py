from typing import Protocol

class Provider(Protocol):
    def clean(self) -> bool:
        """remove unused packages"""
        ...
    def info(self, package:str) -> bool:
        """display information on a specific package"""
        ...
    def install(self, *package:str) -> bool:
        """install a package or series of packages"""
        ...
    def list_installed(self) -> bool:
        """display a list of installed packages"""
        ...
    def remove(self, *package:str) -> bool:
        """remove a package or series of packages"""
        ...
    def search(self, query:str) -> bool:
        """search for packages matching the given search string"""
        ...
    def stats(self) -> bool:
        """display package statistics"""
        ...
    def update(self) -> bool:
        """update the package index"""
        ...
    def upgrade(self) -> bool:
        """upgrade installed packages"""
        ...