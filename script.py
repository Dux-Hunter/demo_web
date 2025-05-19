import streamlit as st

st.set_page_config(page_title="John Murphy Technical Analysis", layout="wide")

menu = st.sidebar.radio("Navigate", (
    "Home", "Introduction", "Charts & Trends", "Patterns", "Indicators", "Market Structure",
    "Cycles & Waves", "Intermarket Analysis", "Full Summary", "Contact"
))

if menu == "Home":
    st.title("📘 Technical Analysis by John Murphy")
    st.markdown("""
    This free online course is based on **John Murphy's book**  
    _"Technical Analysis of the Financial Markets"_.  
    Learn everything from chart basics to advanced trading psychology.
    """)

elif menu == "Introduction":
    st.title("📖 Introduction to Technical Analysis")
    with st.expander("What is Technical Analysis?"):
        st.markdown("""
        - Study of price and volume to forecast future price movement.
        - Focuses on **market action**, not fundamentals.
        - Assumes market discounts everything.
        """)

    with st.expander("Basic Assumptions of TA"):
        st.markdown("""
        1. Market discounts everything  
        2. Prices move in trends  
        3. History tends to repeat itself
        """)

elif menu == "Charts & Trends":
    st.title("📊 Charts & Trends")

    with st.expander("Types of Charts"):
        st.markdown("""
        - **Line Chart**: Simplest form using closing prices.
        - **Bar Chart**: Shows open, high, low, and close (OHLC).
        - **Candlestick Chart**: Visually appealing, shows same OHLC info.
        """)

    with st.expander("Trend Lines"):
        st.markdown("""
        - **Uptrend**: Higher highs and higher lows
        - **Downtrend**: Lower highs and lower lows
        - Drawn across lows in uptrend, highs in downtrend.
        """)

    with st.expander("Support & Resistance"):
        st.markdown("""
        - **Support**: Price level where buying pressure exceeds selling.
        - **Resistance**: Level where selling pressure exceeds buying.
        """)

elif menu == "Patterns":
    st.title("📐 Price Patterns")

    with st.expander("Continuation Patterns"):
        st.markdown("""
        - **Triangles** (Symmetrical, Ascending, Descending)
        - **Flags and Pennants**
        - **Rectangles**
        """)

    with st.expander("Reversal Patterns"):
        st.markdown("""
        - **Head and Shoulders**
        - **Double Top / Double Bottom**
        - **Rounding Bottom**
        """)

elif menu == "Indicators":
    st.title("📈 Technical Indicators")

    with st.expander("Volume Indicators"):
        st.markdown("""
        - **On-Balance Volume (OBV)**
        - **Volume Price Trend (VPT)**
        """)

    with st.expander("Momentum Indicators"):
        st.markdown("""
        - **RSI (Relative Strength Index)**
        - **Stochastics**
        - **MACD (Moving Average Convergence Divergence)**
        """)

    with st.expander("Moving Averages"):
        st.markdown("""
        - Simple Moving Average (SMA)
        - Exponential Moving Average (EMA)
        - Golden Cross & Death Cross
        """)

elif menu == "Market Structure":
    st.title("🏛 Market Structure & Theories")

    with st.expander("Dow Theory"):
        st.markdown("""
        - Markets move in **three trends**
        - **Phases**: Accumulation, Public Participation, Distribution
        - Need **confirmation** from Dow Jones Industrials and Transports
        """)

    with st.expander("Volume and Open Interest"):
        st.markdown("""
        - Volume confirms trend
        - Rising volume = strong trend
        - Open interest used in futures and options markets
        """)

elif menu == "Cycles & Waves":
    st.title("🔁 Cycles and Elliott Wave")

    with st.expander("Cycle Theory"):
        st.markdown("""
        - Markets move in repetitive **cycles**
        - Examples: 4-year cycle, presidential cycle
        """)

    with st.expander("Elliott Wave Theory"):
        st.markdown("""
        - 5-wave impulse + 3-wave correction
        - Waves reflect **crowd psychology**
        - Fractal nature
        """)

elif menu == "Intermarket Analysis":
    st.title("🌐 Intermarket Analysis & Sector Rotation")

    with st.expander("Asset Class Relationships"):
        st.markdown("""
        - Bond → Stocks → Commodities → Gold
        - Intermarket correlations help forecast turning points
        """)

    with st.expander("Sector Rotation"):
        st.markdown("""
        - Early Recovery: Technology, Industrials
        - Mid: Financials, Consumer Discretionary
        - Late: Commodities, Energy
        - Recession: Utilities, Healthcare
        """)

elif menu == "Full Summary":
    st.title("📋 Full Summary of All Topics")
    st.markdown("""
    Click through the sidebar to explore the full John Murphy course, broken into:
    - Trends
    - Indicators
    - Patterns
    - Psychology
    - Practical application
    """)

elif menu == "Contact":
    st.title("📩 Contact Us")
    st.markdown("""
    **Email:** tradetutorial@example.com  
    **YouTube:** [TradingWithTanu](https://youtube.com)  
    **Telegram Group:** t.me/tradingwithtanu
    """)

