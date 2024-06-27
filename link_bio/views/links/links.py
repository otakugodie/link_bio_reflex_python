import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button('LinkedIn', 'Professional Profile', 'https://www.linkedin.com/in/diegorodriguezc'),
        link_button('Facebook', 'Personal Account', 'https://www.facebook.com/otakugodie'),
        link_button('Twitter', 'Personal Account', 'https://x.com/otakugodie'),
        width='100%'
        #rx.button("Click me")
    )