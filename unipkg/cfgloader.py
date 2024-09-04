import tomllib
import pathlib

CFG_DIR = '/etc/pcm/'
CFG_USER_DIR = '~/.config/pcm/'
CFG_FILE = 'pcm.toml'

def load_config():
    p = pathlib.Path(CFG_DIR, CFG_FILE)
    with open(p, 'rb') as fp:
        cfg = tomllib.load(fp)
    p_user = pathlib.Path(CFG_USER_DIR, CFG_FILE)
    if p_user.exists():
        with open(p, 'rb') as fp:
            cfg_user = tomllib.load(fp)
        cfg = { **cfg, **cfg_user }
    return cfg
