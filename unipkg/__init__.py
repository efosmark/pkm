from .provider import Provider
from .cmd import run
from .providers.yay import YayProvider

all_providers:dict[str, type[Provider]] = {
    'yay': YayProvider
}