import streamlit as st
import streamlit_antd_components as sac

from Pages.Home import Home
from Pages.Video_Generation import Video_Generation
from Pages.Stock_Image_Generation import Stock_Image_Generation
from Pages.Image_Generation import Image_Generation
from Pages.Image_Editing import Image_Editing

if "app_name" in st.session_state:
    st.session_state.app_name = "Google"

# from utils.helper_funcs import create_sidebar
st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout="wide",
    menu_items={
        'About': """ Gemini Based Demos for Meesho """
    }
)

with st.sidebar:
    # col1, col2 =  st.columns(2)
    # with col1:
    #     st.image("content/logos/meesho-logo.png", width=140)
    # with col2:
    #     st.image("content/logos/Google-Logo-Large.png", width=100)
    st.image("content/logos/Google-Logo-Large.png", width=100)
    menu_item = sac.menu([
        sac.MenuItem('Home', icon='house-fill'),
        sac.MenuItem('Video Generation', icon="camera-video"),
        sac.MenuItem('Stock Image Generation', icon="image"),
        # sac.MenuItem('Image Generation', icon="headset"),
        sac.MenuItem('Image Editing', icon="pencil-square"),
    ], open_all=True, size="sm", color="orange", variant="left-bar", indent=20, key="menu_item")
page_actions = {
    'Home': Home,
    'Video Generation': Video_Generation,
    'Stock Image Generation': Stock_Image_Generation,
    'Image Generation': Image_Generation,
    'Image Editing': Image_Editing,
}

if menu_item in page_actions.keys():
    page_actions[menu_item]()
