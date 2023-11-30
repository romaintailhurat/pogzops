import httpx
from pogzops.models.envs import PoguesEnv
from pogzops.models.status import Success, Failure, Status
from importlib.resources import files


def base_get(id: str, env: PoguesEnv, url: str) -> Status:
    headers = {}
    headers["Content-Type"] = "application/json"

    if env.token is not None:
        headers["Authorization"] = f"Bearer {env.token}"

    if env.cert_path:
        resp = httpx.get(
            url, headers=headers, verify=files("certs").joinpath("insee-fr-chain.pem")
        )
    else:
        resp = httpx.get(url, headers=headers)

    if resp.status_code == 200:
        print("→ OK")
        return Success(status_code=resp.status_code, payload=resp.json())
    else:
        return Failure(resp.status_code)


def get_questionnaire(id: str, env: PoguesEnv) -> Status:
    url = f"{env.url}/api/persistence/questionnaire/{id}"
    print(f"GET questionnaire {id}")
    print(f"Environnement is {env}")
    print(f"Target URL is {url}")

    return base_get(id, env, url)


def get_lunatic_questionnaire(id: str, env: PoguesEnv) -> Status:
    url = f"{env.url}/api/persistence/questionnaire/json-lunatic/{id}"
    print(f"GET questionnaire {id}")
    print(f"Environnement is {env}")
    print(f"Target URL is {url}")

    return base_get(id, env, url)


def get_questionnaires_by_stamp(stamp: str, env: PoguesEnv):
    url = f"{env.url}/api/persistence/questionnaires/search/meta?owner={stamp}"
    print(f"Environnement is {env}")
    print(f"Target URL is {url}")
    # URK, change the base_get to avoid duplication
    headers = {}
    headers["Content-Type"] = "application/json"

    if env.token is not None:
        headers["Authorization"] = f"Bearer {env.token}"

    if env.cert_path:
        resp = httpx.get(
            url, headers=headers, verify=files("certs").joinpath("insee-fr-chain.pem")
        )
    else:
        resp = httpx.get(url, headers=headers)

    if resp.status_code == 200:
        print("→ OK")
        return Success(status_code=resp.status_code, payload=resp.json())
    else:
        return Failure(resp.status_code)
