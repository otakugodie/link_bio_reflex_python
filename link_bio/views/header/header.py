import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size

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
                    ),
                    rx.hstack(
                        link_icon('https://www.facebook.com/otakugodie'),
                        link_icon('https://x.com/otakugodie'),
                        link_icon('https://www.linkedin.com/in/diegorodriguezc')
                    ),
                    align_items='start'
                )
            ),

            rx.flex(
                info_text('+12', 'years of experience'),
                rx.spacer(),
                info_text('+12', 'years of experience'),
                width='100%'
            ),
            
            
            
            rx.text('I\'m business developer, product leader'),
            spacing='7',
            align_items='start'
        )