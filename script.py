import streamlit as st

# Set page configuration
st.set_page_config(page_title="Trading Tutorial", layout="wide")

# Sidebar navigation
menu = st.sidebar.radio(
    "Navigate",
    ("Home", "Basic Trading Course", "Strategy Guide", "Chart Examples", "Contact")
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

# Basic Trading Course
elif menu == "Basic Trading Course":
    st.title("📚 Basic Trading Course")

    with st.expander("1. What is Trading?"):
        st.markdown("""
        Trading is the act of buying and selling financial instruments like stocks, forex, or crypto for profit.
        
        Types:
        - **Day Trading:** Same day buy/sell
        - **Swing Trading:** Holding for days/weeks
        - **Position Trading:** Long-term holding
        """)

    with st.expander("2. Types of Markets"):
        st.markdown("""
        - **Stock Market:** Shares of companies
        - **Forex Market:** Currency trading
        - **Commodities Market:** Gold, oil, etc.
        - **Crypto Market:** Bitcoin, Ethereum, etc.
        """)

    with st.expander("3. Candlestick Basics"):
        st.markdown("""
        Candlesticks show price movement during a time period.
        
        - Green Candle: Price went up
        - Red Candle: Price went down
        
        Key parts:
        - Body: Open to close
        - Wick: High/low of the period
        """)

    with st.expander("4. Risk Management"):
        st.markdown("""
        - Never risk more than **2% of your capital** on a trade.
        - Use Stop Loss and Take Profit.
        - Maintain a **risk-to-reward ratio** of at least 1:2.
        """)

    with st.expander("5. Psychology of Trading"):
        st.markdown("""
        - Avoid emotional trading.
        - Stick to your plan.
        - Don't chase the market after losses.
        - Keep a **trading journal** to improve.
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
