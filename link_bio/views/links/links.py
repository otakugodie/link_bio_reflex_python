import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button('LinkedIn', 'https://www.linkedin.com/in/diegorodriguezc'),
        link_button('Facebook', 'https://www.facebook.com/otakugodie'),
        link_button('Twitter', 'https://x.com/otakugodie')        
        #rx.button("Click me")
    )