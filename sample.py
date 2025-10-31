import streamlit as st

st.title("Hello World")

st.header("This is a header")
st.subheader("This is a subheader")

st.text("Welcome to Streamlit Session!")

st.markdown("This is a **markdown** text with _italic_ and **bold** formatting.")
st.success("This is a success message!")
st.info("This is an info message.")
st.warning("This is a warning message!")
st.error("This is an error message!")

exp = ZeroDivisionError("This is a custom exception message.")
st.exception(exp)

st.write("This is a simple write statement in Streamlit.")
st.write(range(10))

from PIL import Image
image = Image.open(r"C:\Users\gawas\Downloads\improved_flower.png")
st.image(image, width=300, caption="Sample Image")

if st.checkbox("Show/Hide Text"):
    st.text("You have checked the box!")

status = st.radio("Select your status:", ("Active", "Inactive", "Pending"))
if status == "Active":
    st.success("You are Active!")
elif status == "Inactive":
    st.error("You are Inactive!")
else:
    st.warning("You are Pending!")

items=st.multiselect("Select your favorite fruits:",
                     ["Apple", "Banana", "Mango", "Grapes", "Orange"],
                     default=["Mango", "Grapes"])       
hobby=st.selectbox("Select your hobby:",
                   ["Reading", "Traveling", "Gaming", "Dancing"])

st.write("Your hobby is:", hobby)

st.button("Click Me!")

if st.button("Submit"):
    st.text("Button Clicked!")

name = st.text_input("Enter your name:", "Type here...")
if st.button("Greet Me"):
    result = f"Hello, {name}!"
    st.success(result)

level = st.slider("Select your level:", 1, 10, 5)
st.write("Your level is:", level)