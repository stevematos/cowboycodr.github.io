import reflex as rx
from .style import app_style


class State(rx.State):
    """The app state."""

    pass


def home() -> rx.Component:
    return rx.vstack(
        rx.box(rx.text("Soy Steve Sader Matos Manguinuri")),
        rx.box(rx.text("Python Developer and Software Engineer")),
        class_name="home",
    )


def index() -> rx.Component:
    return rx.vstack(
        home(),
        class_name="index",
    )


app = rx.App(style=app_style)
app.add_page(index)
