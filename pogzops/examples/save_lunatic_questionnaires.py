from remote.get import get_lunatic_questionnaire
from models.envs import PoguesEnv, envs
from json import dump

sandbox_env = PoguesEnv("sandbox", envs["sandbox"])

def title_to_filename(title: str) -> str:
    return title.lower().translate(str.maketrans({" ":"", "-": "_", "(":"_", ")":"_", "é": "e", "à":"a", "=":"_"}))

ids = ["l9o7l439", "ldodefpq", "lix4l70c", "kanye31s1", "kx0a2hn8", "lfsey94u",
       "lb3ei722", "kzfezgxb", "l7j0wwqx", "simpsonsvtl", "kzguw1v7"]

for id in ids:
	status = get_lunatic_questionnaire(id, sandbox_env)
	title = status.payload["label"]["value"]
	file_name = f"{title_to_filename(title)}.lunatic.json"
	with open(f"C:/Users/ARKN1Q/Downloads/TEST/{file_name}", "w", encoding="UTF-8") as json_file:
		dump(status.payload, json_file, ensure_ascii=False)