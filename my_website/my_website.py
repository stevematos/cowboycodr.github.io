import reflex as rx
from .style import get_app_style_from_css
import os


class State(rx.State):
    """The app state."""

    pass


def my_info() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.image(src="/my-pixelart.png"),
            rx.text("Pixelart from video game Stardew Valley"),
            width="20%",
            height="100%",
            class_name="pixelart",
        ),
        rx.box(
            rx.text("I'm Steve Matos"),
            rx.text("I'm a Software Engineer and Python Developer"),
            rx.text(
                "I studied software engineering at the Universidad Nacional Mayor de San Marcos, "
                "and I am curious about gastronomy in general."
            ),
            rx.text("Apart from coding, some other activities that I love to do!"),
            rx.list.unordered(
                rx.list.item("Playing Video Games."),
                rx.list.item("Watch anime, series and movies."),
                rx.list.item("Play with my cats."),
            ),
            width="80%",
            height="100%",
        ),
        spacing="1",
        width="100%",
    )


def home() -> rx.Component:
    return rx.vstack(
        my_info(),
        class_name="home",
    )


def footer() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Using Reflexs",
            white_space="normal",
            text_align="center",
        ),
        align="center",
    )


def index() -> rx.Component:
    return rx.vstack(
        home(),
        footer(),
        class_name="index",
    )


def get_static_path():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_path = os.path.join(base_dir, "assets")
    return static_path


app = rx.App(
    style=get_app_style_from_css(f"{get_static_path()}/styles.css"),
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="teal",
    ),
)

app.add_page(index)
