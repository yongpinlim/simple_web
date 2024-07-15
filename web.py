import streamlit as st
import functions


todos = functions.read_file()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_file(todos)


st.title("My To-do App")
st.subheader("My first simple web application")
st.write("Just for testing")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()



st.text_input(label="", placeholder="Please add more to do list",
              on_change=add_todo, key="new_todo")

st.write(st.session_state)