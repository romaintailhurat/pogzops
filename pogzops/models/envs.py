from dataclasses import dataclass
from pathlib import Path

@dataclass
class PoguesEnv:
    name: str
    url: str
    token: str = None
    cert_path: bool = False

    def __str__(self) -> str:
        tk = "No token" if self.token is None else self.token[0:6]
        cp = "No cert path" if not self.cert_path else f"Cert path is {self.cert_path}"
        return f"PoguesEnv {self.name} - {self.url} - {tk} - {cp}"

@dataclass
class EnvsState:
    source_env: PoguesEnv
    target_env: PoguesEnv

envs = {
    "prod-interne" : "https://api.conception-questionnaires.insee.fr",
    "enl": "https://pogues-back-office-enl-queenv1.dev.kube.insee.fr",
    "beta" : "https://pogues-back-office-beta-testeurs.demo.insee.io",
    "demo" : "https://pogues-back-office.demo.insee.io",
    "enl" : "https://pogues-back-office-enl-queenv1.dev.kube.insee.fr",
    "recette": "https://api-conception-questionnaires.recette.insee.fr/rmes-pogbo",
    "sandbox": "https://pogues-back-office-sandbox.demo.insee.io"
}