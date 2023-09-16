import streamlit as st
from streamlit_option_menu import option_menu


def _init_state():
    st.session_state.setdefault("input_fields", [""])
    st.session_state.setdefault("shopping_items", [])
    st.session_state.setdefault("ingridients", ["Fish", "Tomato", "Onion"])
    st.session_state.setdefault(
        "products", ["MBudget Fish", "MBudget Tomato", "MBudget Onion"])

    # Flag to control visibility of input fields
    st.session_state.setdefault("show_fields", True)
    st.session_state.setdefault("show_ingridients", False)
    st.session_state.setdefault("show_products", False)


# The main function to run the app


def main():

    selected2 = option_menu(None, ["Shop", "Cook"],
                            icons=["shop", "list-task"],
                            menu_icon="cast", default_index=0, orientation="horizontal")

    st.title(selected2)

    st.sidebar.title("About")
    st.sidebar.text("This is an emulated multi-tab Q&A interface.")

    # Initialize session state
    _init_state()

    if selected2 == 'Shop':

        # Show the subtitle, input fields, and buttons only if show_fields is True
        if st.session_state.show_fields:
            st.subheader("What do you want to buy?")

            # Display existing input fields
            for idx, field in enumerate(st.session_state.input_fields):
                st.session_state.input_fields[idx] = st.text_input(
                    f"Item {idx + 1}", field)

            # Add a new input field when the button is clicked
            if st.button("Add another item"):
                st.session_state.input_fields.append("")

            # Button to submit items
            if st.button("Submit"):
                # Only add non-empty items
                st.session_state.shopping_items += [
                    item for item in st.session_state.input_fields if item]
                # Clear all input fields and buttons
                st.session_state.input_fields = []
                st.session_state.show_fields = False  # Hide input fields and buttons

        # Display shopping list
        st.subheader("Shopping List:")
        for item in st.session_state.shopping_items:
            st.write(item)

    if selected2 == 'Cook':
        st.subheader("What do you want to cook?")
        st.text_input("")
        if st.button("Create Ingridients"):
            st.session_state.show_ingridients = True  # Show ingridients
        if st.session_state.show_ingridients:
            st.subheader("Ingridients:")
            for item in st.session_state.ingridients:
                st.write(item)
            if st.button("Show Products"):
                st.session_state.show_products = True  # Show ingridients
                st.subheader("Products:")
                for item in st.session_state.products:
                    st.write(item)


# Call the main function
if __name__ == "__main__":
    main()
