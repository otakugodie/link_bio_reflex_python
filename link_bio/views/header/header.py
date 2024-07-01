import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
            rx.hstack(
                rx.avatar(
                    fallback="DR", 
                    size='5'
                ),
                rx.vstack(
                    rx.heading(
                        'Diego Rodriguez', 
                        size='5'
                    ),
                    rx.text(
                        '@otakugodie', 
                        size='3',
                        margin_top='0px !important'
                    )
                )
            ),
            rx.text('I\'m business developer, product leader'),
            align_items='start'
        )