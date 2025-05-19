import streamlit as st

# Set page configuration
st.set_page_config(page_title="Trading Tutorial", layout="wide")

# Sidebar navigation
menu = st.sidebar.radio(
    "Navigate",
    ("Home", "Strategy Guide", "Chart Examples", "Contact")
)

# Home Page
if menu == "Home":
    st.title("📈 Welcome to the Trading Tutorial Website")
    st.markdown("""
        Learn how to trade smartly and manage risk with our beginner-friendly guides and examples.
        
        This tutorial covers:
        - Basic trading concepts
        - Chart reading
        - Strategies for intraday and swing trading
        - Journaling your trades
    """)

# Strategy Guide Page
elif menu == "Strategy Guide":
    st.title("📘 Trading Strategies")
    st.subheader("1. Support & Resistance")
    st.markdown("""
        - Support: Price level where buyers step in.
        - Resistance: Price level where sellers step in.
    """)

    st.subheader("2. Moving Averages (MA)")
    st.markdown("""
        - 50 MA and 200 MA are commonly used.
        - Golden cross = Buy signal.
        - Death cross = Sell signal.
    """)

    st.subheader("3. RSI Indicator")
    st.markdown("""
        - RSI < 30: Oversold (potential buy)
        - RSI > 70: Overbought (potential sell)
    """)

# Chart Examples Page
elif menu == "Chart Examples":
    st.title("📊 Chart Examples")

    st.markdown("Here you can upload or display chart screenshots.")
    uploaded_file = st.file_uploader("Upload your trading chart", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Chart", use_column_width=True)

# Contact Page
elif menu == "Contact":
    st.title("📩 Contact Us")
    st.markdown("""
        - **Email:** tradetutorial@example.com  
        - **YouTube:** [TradingWithTanu](https://youtube.com)  
        - **Telegram Group:** t.me/tradingwithtanu
    """)
