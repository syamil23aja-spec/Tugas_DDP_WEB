import streamlit as st

def init_db():
    if 'debts' not in st.session_state:
        st.session_state.debts = [
            {
                "id": "KBN-001",
                "customerName": "Ibu Siti",
                "phoneNumber": "08123456789",
                "totalDebt": 150000,
                "transactionDate": "2026-11-01",
                "dueDate": "2026-11-30",
                "items": "Beras 5kg, Minyak",
                "status": "Belum Lunas"
            }
        ]