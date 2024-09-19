from .provider import Provider
from .cmd import run
from .providers.yay import YayProvider
from .providers.pacman import PacmanProvider
from .providers.apt import AptProvider

all_providers:dict[str, type[Provider]] = {
    'yay': YayProvider,
    'pacman': PacmanProvider,
    'apt': AptProvider,
}