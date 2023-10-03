from json import load
from importlib.resources import files

# TODO implement an internal load and an external
def load_secrets():
    with files("conf").joinpath("secrets.json").open('r', encoding="UTF-8") as sf:
        secrets = load(sf)
    
    return secrets

def load_conf():
    with files("conf").joinpath("conf.json").open('r', encoding="UTF-8") as cf:
        conf = load(cf)
    return conf