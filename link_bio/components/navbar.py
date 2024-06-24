import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            'diegofer',
            height='40px',
            color_scheme='cyan'
        ),
        position='sticky',
        bg='blue',
        padding_x='16px',
        padding_y='8px',
        z_index='999'
    )