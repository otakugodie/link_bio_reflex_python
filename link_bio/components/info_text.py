import reflex as rx
from link_bio.styles.styles import Size as Size

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            as_='span',
            color_scheme='ruby'
        ),
        f" {body}", font_size=Size.MEDIUM.value
    )