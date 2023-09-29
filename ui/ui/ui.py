"""
Pogzops web ui
    - Color palette : https://coolors.co/palette/ff595e-ffca3a-8ac926-1982c4-6a4c93
"""
from rxconfig import config
import reflex as rx

from pogzops.models.envs import PoguesEnv, envs

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""    
    source_env_name: str = "demo"
    target_env_name: str = "prod-interne"
    
    def change_source_env(self, new_env: str):
        self.source_env_name = new_env

    @rx.var
    def source(self) -> str: # TODO useful ?
        return self.source_env_name

def envs_card() -> rx.Component:
    content = rx.vstack(
        rx.heading("Envs", size="lg"),
        rx.text("Manage Pogues environments"),
        rx.hstack(rx.text("Current source env is:"), rx.text(State.source_env_name)),
        rx.link(rx.button("Go"), href="/environments", color="#1982C4", button=True)
    )
    return rx.grid_item(content, row_span=1, col_span=1)

def remote_card() -> rx.Component:
    return rx.grid_item(rx.heading("Remote", size="lg") , row_span=1, col_span=1)

def local_card() -> rx.Component:
    return rx.grid_item(rx.heading("Local", size="lg") , row_span=1, col_span=1)

# --- Pages
def index() -> rx.Component:
    return rx.vstack(
        rx.heading("Pogzops", size="4xl", color="#6A4C93"),
        rx.grid(
            envs_card(),
            remote_card(),
            local_card(),
            template_columns="repeat(3, 1fr)",
            width="100%"
        )
    )

def environments() -> rx.Component:
    return rx.vstack(
        rx.heading("Pogzops", size="4xl", color="#6A4C93")
    )
        

# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index)
app.add_page(environments)
app.compile()