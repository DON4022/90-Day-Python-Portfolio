import streamlit as st

# =====================================================================
# PORTFOLIO LIVE PAGE: IT Infrastructure Budget Estimator
# =====================================================================

# Webpage Heading Configuration
st.set_page_config(page_title="Infrastructure Estimator", page_icon="💻")
st.title("💻 Systems Resource & Budget Estimator")
st.markdown("---")

# 1. WEB INPUT LAYER (Replacing terminal input() with graphic sliders and input fields)
project_name = st.text_input("Project Deployment Name:", value="Alpha Cloud Cluster")

# Columns for a clean horizontal dashboard layout
col1, col2 = st.columns(2)

with col1:
    nodes = st.number_input("Number of Cloud Server Nodes:", min_value=1, max_value=100, value=5)
    days = st.number_input("Deployment Timeline (Days):", min_value=1, max_value=365, value=30)

with col2:
    daily_rate = st.number_input("Daily Hosting Cost per Node ($):", min_value=0.0, max_value=1000.0, value=12.50, step=0.50)

# 2. PROCESSING LAYER (The exact same math logic as day2.py!)
total_hosting_cost = nodes * daily_rate * days
average_cost_per_day = total_hosting_cost / days
is_funded = total_hosting_cost > 0

# 3. WEB OUTPUT LAYER (Displaying data dynamically on the page)
st.markdown("### 📊 System Technical Ledger")

# Visual data cards
st.metric(label="TOTAL PROJECT BUDGET", value=f"${total_hosting_cost:,.2f}")
st.metric(label="Average Burn Rate per Day", value=f"${average_cost_per_day:,.2f}")

# Structural breakdown table
st.markdown(f"""
| System Metric | Logged Status |
| :--- | :--- |
| **Target Project** | {project_name.upper()} |
| **Infrastructure Scalability** | {nodes} Active Nodes |
| **Operational Lifecycle** | {days} Days |
| **System Funding Verification Flag** | `{is_funded}` |
""")
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