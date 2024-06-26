import reflex as rx

def link_button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(text, width='100%'),
        href=url,
        is_external=True,
        width='100%'

    )
