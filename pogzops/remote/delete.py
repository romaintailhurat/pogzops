import httpx
from models.envs import PoguesEnv
from models.status import Success, Failure
from importlib.resources import files


def delete_questionnaire(url: str, env: PoguesEnv):
    headers = {}
    headers["Content-Type"] = "application/json"

    if env.token is not None:
        headers["Authorization"] = f"Bearer {env.token}"

    if env.cert_path:
        resp = httpx.delete(
            url, headers=headers, verify=files("certs").joinpath("insee-fr-chain.pem")
        )
    else:
        resp = httpx.delete(url, headers=headers)

    if resp.status_code == 200:
        print("→ OK")
        return Success(status_code=resp.status_code, payload=resp.json())
    else:
        return Failure(resp.status_code)
