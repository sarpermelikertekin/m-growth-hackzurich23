import streamlit as st
from streamlit_option_menu import option_menu


########## States ##########
def _init_state():

    ########## Shop Tab ##########
    st.session_state.setdefault("shop_input_fields", [""])
    st.session_state.setdefault("shop_shopping_items", [])

    st.session_state.setdefault("shop_show_fields", True)

    ########## Cook Tab ##########
    st.session_state.setdefault(
        "cook_ingridients", ["Fish", "Tomato", "Onion"])
    st.session_state.setdefault(
        "cook_products", ["MBudget Fish", "MBudget Tomato", "MBudget Onion"])

    ########## Stars Tab ##########
    st.session_state.setdefault("points", 50)  # Added for Stars tab

    ########## SideBar ##########
    st.session_state.setdefault("cook_show_init", True)
    st.session_state.setdefault("cook_show_ingridients", False)
    st.session_state.setdefault("cook_show_products", False)


def main():

    # Initialize session state
    _init_state()

    tab = option_menu(None, ["Shop", "Cook", "Stars"],
                      icons=["shop", "list-task", "star"],
                      menu_icon="cast", default_index=0, orientation="horizontal")

    st.title(tab)

    ########## SideBar ##########
    st.sidebar.title("User Preferences")
    st.sidebar.write("Let us recommend the best products for you")

    # Sliders
    sustainability_score = st.sidebar.slider('Sustainability', 1, 5, 3)
    price_score = st.sidebar.slider('Price', 1, 5, 3)

    ########## Shop Tab ##########

    if tab == 'Shop':
        # Show the subtitle, input fields, and buttons only if shop_show_fields is True
        if st.session_state.shop_show_fields:
            st.subheader("What do you want to buy?")

            # Display existing input fields
            for idx, field in enumerate(st.session_state.shop_input_fields):
                st.session_state.shop_input_fields[idx] = st.text_input(
                    f"Item {idx + 1}", field)

            # Add a new input field when the button is clicked
            if st.button("Add another item"):
                st.session_state.shop_input_fields.append("")

            # Button to submit items
            if st.button("Submit"):
                # Only add non-empty items
                st.session_state.shop_shopping_items += [
                    item for item in st.session_state.shop_input_fields if item]
                # Clear all input fields and buttons
                st.session_state.shop_input_fields = []
                st.session_state.shop_show_fields = False
                st.subheader("Shopping List:")

        # Display shopping list
        for item in st.session_state.shop_shopping_items:
            st.write(item)

    ########## Cook Tab ##########

    if tab == 'Cook':
        if st.session_state.cook_show_init:
            st.subheader("What do you want to cook?")
            st.text_input("")
            if st.button("Give me the Ingridients"):
                st.session_state.cook_show_ingridients = True
        if st.session_state.cook_show_ingridients:
            st.subheader("Ingridients:")
            for item in st.session_state.cook_ingridients:
                st.write(item)
            if st.button("Show Products"):
                st.session_state.cook_show_products = True
        if st.session_state.cook_show_products:
            st.subheader("Products:")
            for item in st.session_state.cook_products:
                st.write(item)

    ########## Stars Tab ##########

    if tab == 'Stars':
        st.subheader("Collect your reward")

        st.write("Total Points: " + str(st.session_state.points))

        cards = [
            {"name": "Tee", "points_needed": 30},
            {"name": "Kaffe", "points_needed": 50},
            {"name": "Urlaub", "points_needed": 70},
        ]

        for card in cards:
            st.markdown(f"### {card['name']}")
            st.markdown(f"Points needed: {card['points_needed']}")


# Call the main function
if __name__ == "__main__":
    main()
