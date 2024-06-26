import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
import link_bio.styles.styles as styles

# from rxconfig import config
class State(rx.State):
    pass

def index() -> rx.Component:
    #return rx.text('Hi Reflex', color='blue')
    return rx.center(
        rx.box(
            navbar(),        
            rx.center(
                rx.vstack(        
                    header(),
                    links(),
                    max_width=styles.MAX_WIDTH,
                    width='100%',
                    margin_y=styles.Spacer.BIG
                )
            ),                
            footer()
        )
     )

    
    


app = rx.App()
app.add_page(index)
app._compile()



"""
class State(rx.State):
    ...

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Hi Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
"""