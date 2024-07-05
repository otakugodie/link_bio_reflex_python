import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico", width="100px", height="auto"),
        rx.link(
            f'© 2023-{datetime.date.today().year} by DiegoR', 
            href="https://www.google.com", 
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            'This is a footer',
            font_size=Size.MEDIUM.value,
            margin_top='0px !important'
        ),
        margin_bottom=Size.BIG.value
    )