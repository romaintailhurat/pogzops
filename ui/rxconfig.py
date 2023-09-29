import reflex as rx

class UiConfig(rx.Config):
    pass

config = UiConfig(
    app_name="ui",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)