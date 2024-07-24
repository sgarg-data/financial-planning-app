import streamlit as st
import numpy as np

def mortgage_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    number_of_payments = years * 12
    payment = principal * (monthly_rate * (1 + monthly_rate) ** number_of_payments) / ((1 + monthly_rate) ** number_of_payments - 1)
    return payment

def future_value(pv, annual_rate, years):
    return pv * (1 + annual_rate) ** years

def present_value(fv, annual_rate, years):
    return fv / (1 + annual_rate) ** years

# Streamlit app
st.title('Financial Planning Calculator')

# Inputs
house_price = st.number_input('House Price (AED)', min_value=0, value=2000000)
downpayment_percentage = st.number_input('Down Payment Percentage', min_value=0.0, max_value=1.0, value=0.20)
loan_term_years = st.number_input('Loan Term (Years)', min_value=1, value=10)
annual_loan_rate = st.number_input('Annual Loan Interest Rate (%)', min_value=0.0, value=3.0)
children_education_amount = st.number_input('Children\'s Education Amount (AED)', min_value=0, value=1000000)
education_years = st.number_input('Years to Accumulate Education Fund', min_value=1, value=20)
annual_inflation_rate = st.number_input('Annual Inflation Rate (%)', min_value=0.0, value=7.0) / 100
investment_return_rate = st.number_input('Annual Investment Return Rate (%)', min_value=0.0, value=5.0) / 100
monthly_expenses = st.number_input('Monthly Expenses (AED)', min_value=0, value=13000)
current_income = st.number_input('Current Monthly Income (AED)', min_value=0, value=25000)

# Calculations
downpayment = house_price * downpayment_percentage
loan_amount = house_price - downpayment
monthly_mortgage_payment = mortgage_payment(loan_amount, annual_loan_rate, loan_term_years)

future_education_amount = future_value(children_education_amount, annual_inflation_rate, education_years)
present_value_needed_for_education = present_value(future_education_amount, investment_return_rate, education_years)

total_cash_needed = downpayment + present_value_needed_for_education

monthly_deficit = monthly_mortgage_payment + monthly_expenses - current_income
total_deficit_amount = monthly_deficit * 12 * loan_term_years

total_extra_cash_needed = total_cash_needed + total_deficit_amount

# Display results
st.subheader('Results')
st.write(f"**Down Payment:** {downpayment:.2f} AED")
st.write(f"**Monthly Mortgage Payment:** {monthly_mortgage_payment:.2f} AED")
st.write(f"**Future Value of Education Fund (in {education_years} years):** {future_education_amount:.2f} AED")
st.write(f"**Present Value Needed for Education Fund:** {present_value_needed_for_education:.2f} AED")
st.write(f"**Total Cash Required:** {total_cash_needed:.2f} AED")
st.write(f"**Monthly Deficit:** {monthly_deficit:.2f} AED")
st.write(f"**Total Deficit Amount (for {loan_term_years} years):** {total_deficit_amount:.2f} AED")
st.write(f"**Total Extra Cash Needed:** {total_extra_cash_needed:.2f} AED")
