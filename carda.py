from streamlit_card import card

res = card(
    title="Streamlit Card",
    text="This is a test card",
    image="https://placekitten.com/500/500",
    styles={
        "card": {
            "width": "500px",
            "height": "500px",
            "border-radius": "60px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
        },
        "filter": {
            "background-color": "rgba(0, 0, 0, 0)"  # <- make the image not dimmed anymore
        }
    }
)