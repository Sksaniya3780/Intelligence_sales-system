import streamlit as st


def page_title(title):

    st.title(title)


def section_header(text):

    st.subheader(text)


def success_message(text):

    st.success(text)


def warning_message(text):

    st.warning(text)