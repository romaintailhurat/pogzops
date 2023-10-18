from dataclasses import dataclass

@dataclass
class PoguesEnv:
    name: str
    url: str
    token: str | None = None
    cert_path: bool = False

    def __str__(self) -> str:
        tk = "No token" if self.token is None else self.token[0:6]
        cp = "No cert path" if not self.cert_path else f"Cert path is {self.cert_path}"
        return f"PoguesEnv {self.name} - {self.url} - {tk} - {cp}"
