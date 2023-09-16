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

    ########## SideBar ##########
    st.session_state.setdefault("cook_show_ingridients", False)
    st.session_state.setdefault("cook_show_products", False)


def main():

    # Initialize session state
    _init_state()

    tab = option_menu(None, ["Shop", "Cook"],
                      icons=["shop", "list-task"],
                      menu_icon="cast", default_index=0, orientation="horizontal")

    st.title(tab)

    ########## SideBar ##########
    st.sidebar.title("User Preferences")
    st.sidebar.write("Let us recommend the best products for you")

    # Sliders
    sustainability_score = st.sidebar.slider('Sustainability', 1, 5, 3)
    price_score = st.sidebar.slider('Price', 1, 5, 3)

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

        # Display shopping list
        st.subheader("Shopping List:")
        for item in st.session_state.shop_shopping_items:
            st.write(item)

    if tab == 'Cook':
        st.subheader("What do you want to cook?")
        st.text_input("")
        if st.button("Create Ingridients"):
            st.session_state.cook_show_ingridients = True  # Show cook_ingridients
        if st.session_state.cook_show_ingridients:
            st.subheader("Ingridients:")
            for item in st.session_state.cook_ingridients:
                st.write(item)
            if st.button("Show Products"):
                st.session_state.cook_show_products = True  # Show cook_products
                st.subheader("Products:")
                for item in st.session_state.cook_products:
                    st.write(item)


# Call the main function
if __name__ == "__main__":
    main()
