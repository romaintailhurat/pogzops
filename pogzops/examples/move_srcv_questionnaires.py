from models.envs import PoguesEnv, envs
from importlib.resources import files
from remote.opz import copy
from json import load

with files("secrets").joinpath("secrets.json").open('r', encoding="UTF-8") as sf:
	secrets = load(sf)

beta_env = PoguesEnv("beta", envs["beta"])
prod_env = PoguesEnv(
    "prod-interne", 
    envs["prod-interne"], 
    token=secrets["tokens"]["mine"],
    cert_path=True)


srcv_ids = ["lkuyylbx", "lj7683a6"]

for id in srcv_ids:
    copy(id, beta_env, prod_env)