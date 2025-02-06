from .provider import Provider
from .cmd import run
from .providers.yay import YayProvider
from .providers.pacman import PacmanProvider
from .providers.apt import AptProvider

# TODO: this could be a dynamic look into the providers sub-package.
all_providers:dict[str, type[Provider]] = {
    'yay': YayProvider,
    'pacman': PacmanProvider,
    'apt': AptProvider,
}