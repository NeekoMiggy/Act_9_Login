st.title("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "secret":
        st.success("You have successfully logged in!")
    else:
        st.error("Invalid credentials")
