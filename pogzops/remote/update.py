import httpx
from pogzops.models.envs import PoguesEnv
from importlib.resources import files
from pogzops.models.status import Success, Failure, Status


def update_questionnaire(questionnaire_json: dict, id: str, env: PoguesEnv) -> Status:
    print(f"PUT questionnaire {id}")
    print(f"Environnement is {env}")

    url = f"{env.url}/api/persistence/questionnaire/{id}"
    headers = {}
    headers["Content-Type"] = "application/json"

    if env.token is not None:
        headers["Authorization"] = f"Bearer {env.token}"

    if env.cert_path:
        resp = httpx.put(
            url,
            json=questionnaire_json,
            headers=headers,
            verify=files("certs").joinpath("insee-fr-chain.pem"),
        )
    else:
        resp = httpx.put(url, json=questionnaire_json, headers=headers)

    if httpx.codes.is_success(resp.status_code):
        print("→ OK")
        return Success(resp.status_code)
    else:
        print(f"Error, status is {str(resp.status_code)}")
        return Failure(resp.status_code)
