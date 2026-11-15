import streamlit as st
from db import init_db

st.set_page_config(page_title="Sistem Manajemen Piutang Warung", layout="wide")

# Inisialisasi Tempat Penyimpanan Bersama 
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

st.title("📊 Dashboard Utama ")
st.markdown("Ringkasan kondisi keuangan dan total piutang warung.")

debts = st.session_state.debts
total_piutang = sum(d['totalDebt'] for d in debts if d['status'] == 'Belum Lunas')
total_pelanggan = len(debts)
kasbon_belum_lunas = len([d for d in debts if d['status'] == 'Belum Lunas'])

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Piutang Aktif", f"Rp {total_piutang:,.0f}")
with col2:
    st.metric("Total Pelanggan Tercatat", f"{total_pelanggan} Orang")
with col3:
    st.metric("Kasbon Belum Lunas", f"{kasbon_belum_lunas} Kasus")