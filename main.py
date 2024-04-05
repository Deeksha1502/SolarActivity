import streamlit as st
st. set_page_config(layout="wide")



with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',
         unsafe_allow_html=True  )


st.markdown(
    """
    <style>
    .navbar {
        display: flex;
        background-color: #333;
        padding: 10px;
    }
    .nav-item {
        margin-right: 20px;
        text-color:white;
    }
    a {
        color: white;
        text-decoration: none;
    }
    </style>
    """
    , unsafe_allow_html=True
)

st.markdown("""
            
             
     <div class="navbar">
        <div class="nav-item">
            <a href="/">Home</a>
        </div>
        <div class="nav-item">
            <a href="/page1">Page 1</a>
        </div>
        <div class="nav-item">
            <a href="/page2">Page 2</a>
        </div>
    </div>
       
    """
 , unsafe_allow_html=True)

st.image('background.jpeg')