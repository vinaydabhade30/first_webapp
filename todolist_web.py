import streamlit as st
import function_mod

todos = function_mod.file_open_r()


def add_todo():
    todo_item = st.session_state['text'] + "\n"
    todos.append(todo_item)
    function_mod.file_open_w(todos)


# st.title('Om Namha Shivaya')

st.title('My Todo app')
st.subheader("this my todo app")
st.write("This app is increase your productivity")

for index, todo in enumerate (todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        st.info("Sure your take is done")
        todos.pop(index)
        function_mod.file_open_w(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label='', placeholder="add_todo", on_change=add_todo, key='text')

#st.session_state