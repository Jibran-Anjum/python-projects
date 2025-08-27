import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    print(todo)
    todos.append(todo + "\n")
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todos app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Input Please:",
              placeholder="Enter a todo...",
              on_change=add_todo, key="new_todo")

st.session_state