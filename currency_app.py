import streamlit as st

# =====================================================================
# PORTFOLIO ASSET 2: Global Currency Exchange & Fee Engine
# ARCHITECTURE: Procedural / Input-Process-Output (IPO)
# DATA TYPES EXPLORED: String, Integer, Float, Boolean, Casting
# =====================================================================

# 1. APPLICATION HEADER INTERFACE
st.set_page_config(page_title="Currency Ledger Engine", page_icon="💱")
st.title("💱 Global Currency Exchange & Transaction Engine")
st.markdown("---")

st.markdown("### 📥 Transaction Configuration Layer")

# 2. INPUT LAYER (Capturing data via graphic selectors)
base_currency = st.text_input("Source Currency Code (e.g., USD, EUR, KSH):", value="USD")
target_currency = st.text_input("Target Currency Code:", value="EUR")

col1, col2 = st.columns(2)

with col1:
    # Capturing raw whole numbers and decimals
    amount_to_exchange = st.number_input("Amount to Exchange:", min_value=1.0, value=100.0, step=10.0)
    exchange_rate = st.number_input(f"Exchange Rate (1 {base_currency} to {target_currency}):", min_value=0.0001, value=0.92, format="%.4f")

with col2:
    # A flat fee in the target currency (Float)
    transaction_fee = st.number_input("Standard Transaction Fee ($):", min_value=0.0, value=2.50, step=0.50)
    # A processing limit check (Integer)
    daily_limit = st.number_input("Account Daily Transaction Limit Count:", min_value=1, value=10)

# 3. PROCESSING LAYER (The Core Mathematics Engine)
# Explicit Type Casting to protect memory calculations
amount = float(amount_to_exchange)
rate = float(exchange_rate)
fee = float(transaction_fee)
limit_count = int(daily_limit)

# Mathematical Operators (*, -)
raw_converted_amount = amount * rate
final_payout = raw_converted_amount - fee

# Boolean Logic Flag (System Safety Constraints)
# Checks if the transaction size is valid (payout must be greater than zero)
is_transaction_safe = final_payout > 0

# 4. OUTPUT LAYER (Dynamic User Interface & Structural Reporting)
st.markdown("### 📊 Financial Settlement Ledger")

# Visual KPI Cards for Critical Metrics
st.metric(label=f"TOTAL RECEIVABLE ({target_currency})", value=f"{final_payout:,.2f} {target_currency}")
st.metric(label="System Processing Fee", value=f"${fee:,.2f}")

# System Architecture Diagnostics Table
st.markdown("#### ⚙️ Memory & System Type Auditing")
st.markdown(f"""
| System Metric Block | Live Value | Core Data Type Class |
| :--- | :--- | :--- |
| **Trading Pair** | {base_currency.upper()} / {target_currency.upper()} | `<class 'str'>` |
| **Raw Exchange Product** | {raw_converted_amount:,.4f} | `{type(raw_converted_amount)}` |
| **Daily Throttle Limit** | {limit_count} transfers allowed | `{type(limit_count)}` |
| **Safety Clearance Flag** | `{is_transaction_safe}` | `{type(is_transaction_safe)}` |
""")