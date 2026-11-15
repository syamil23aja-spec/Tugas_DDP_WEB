import streamlit as st
from db import init_db
from datetime import datetime

st.title("📝 Formulir Tambah Kasbon Baru (Anggota 2)")

if 'debts' not in st.session_state:
    st.session_state.debts = []

with st.form("form_kasbon"):
    nama = st.text_input("Nama Pelanggan")
    hp = st.text_input("Nomor HP / WhatsApp")
    nominal = st.number_input("Nominal Kasbon (Rp)", min_value=0, step=1000)
    jatuh_tempo = st.date_input("Tanggal Jatuh Tempo")
    barang = st.text_area("Barang yang Dibeli")
    
    submit = st.form_submit_button("Simpan Kasbon")
    if submit:
        if nama and nominal > 0:
            new_entry = {
                "id": f"KBN-{int(datetime.now().timestamp())}",
                "customerName": nama,
                "phoneNumber": hp,
                "totalDebt": int(nominal),
                "transactionDate": str(datetime.now().date()),
                "dueDate": str(jatuh_tempo),
                "items": barang,
                "status": "Belum Lunas"
            }
            st.session_state.debts.append(new_entry)
            st.success("Data kasbon berhasil disimpan!")
        else:
            st.error("Mohon isi nama dan nominal dengan benar.")