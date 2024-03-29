from models.envs import PoguesEnv
from remote.opz import change_stamp, copy
from conf.conf import load_secrets, load_conf
from remote.get import get_questionnaires_by_stamp
from remote.delete import delete_questionnaire
import re

from yaml import safe_load

secrets = load_secrets()
conf = load_conf()
envs = conf["envs"]

beta = "beta"
prod = "prod-interne"
demo = "demo"
recette = "recette"

beta_env = PoguesEnv(beta, envs[beta])
prod_env = PoguesEnv(prod, envs[prod], token=secrets["tokens"]["mine"], cert_path=True)
demo_env = PoguesEnv(demo, envs[demo])
enl_env = PoguesEnv("enl", envs["enl"], cert_path=True)
recette_env = PoguesEnv(recette, envs[recette], cert_path=True)
sandbox_env = PoguesEnv("sandbox", envs["sandbox"])

# ------- RUN
""" save in /examples?
from remote.opz import check_duplicates_from_api
from remote.get import get_questionnaire 
from output.reporting import generate_duplicate_report, save_report
from pathlib import Path

status = get_questionnaire("lkuwq18g", prod_env)

if status.is_success():
	refs = status.payload["childQuestionnaireRef"]
	duplicates = check_duplicates_from_api(refs, prod_env)
	report = generate_duplicate_report(duplicates)
	save_report(report, Path("C:/Users/ARKN1Q/Downloads"))
"""

"""
qs_status = get_questionnaires_by_stamp("FAKEPERMISSION", demo_env)

pattern = re.compile(r"20\d{2}")

if qs_status.is_success():
    for questionnaire in qs_status.payload:
        raw_date = questionnaire["lastUpdatedDate"]
        s = pattern.search(raw_date)
        if s is not None:
            year = s.group()
            if year == "2022":
                del_url = f"{demo_env.url}/api/persistence/questionnaire/{questionnaire['id']}"
                print(questionnaire["Label"][0])
                print(del_url)
                status = delete_questionnaire(del_url, demo_env)
"""


# TCM

ctrps_modules_id = ["ljx26aw3", "ljsc4ej1"]

for module_id in ctrps_modules_id:
    result = copy(module_id, prod_env, demo_env)
    print(result)
