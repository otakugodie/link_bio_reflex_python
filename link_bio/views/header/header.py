import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="DR", size='5'),
        rx.text('@otakugodie'),
        rx.text('HI 👋, MY NAME IS DIEGO RODRÍGUEZ'),
        rx.text('I\'m business developer, product leader')
    )

    