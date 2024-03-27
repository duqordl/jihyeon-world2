import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

# # Page title
# st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
# st.title('📊 Interactive Data Explorer')

# st.sidebar.title('Sidebar title')

# st.title("this is the app title")
# st.header("this is the markdown")
# st.markdown("this is the header")
# st.subheader("this is the subheader")
# st.caption("this is the caption")
# st.code("x=2021")
# st.latex(r'''a+ar^1+ar^2+ar^3''')

rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)