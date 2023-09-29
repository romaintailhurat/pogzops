from models.envs import PoguesEnv, envs
from models.status import Success
from remote.opz import check_duplicates_from_api
from remote.get import get_questionnaire
from output.reporting import generate_duplicate_report, save_report

from json import load
from importlib.resources import files
from pathlib import Path


with files("secrets").joinpath("secrets.json").open('r', encoding="UTF-8") as sf:
	secrets = load(sf)

# Useful envs

beta = "beta"
prod = "prod-interne"
demo = "demo"
recette = "recette"

beta_env = PoguesEnv(beta, envs[beta])
prod_env = PoguesEnv(
    prod, 
    envs[prod], 
    token=secrets["tokens"]["mine"],
    cert_path=True)
demo_env = PoguesEnv(demo, envs[demo])
enl_env = PoguesEnv("enl", envs["enl"], cert_path=True)
recette_env = PoguesEnv(recette, envs[recette], cert_path=True)
sandbox_env = PoguesEnv("sandbox", envs["sandbox"])

# ------- RUN

status = get_questionnaire("lkuwq18g", prod_env)

if type(status) is Success:
	refs = status.payload["childQuestionnaireRef"]
	duplicates = check_duplicates_from_api(refs, prod_env)
	report = generate_duplicate_report(duplicates)
	save_report(report, Path("C:/Users/ARKN1Q/Downloads"))