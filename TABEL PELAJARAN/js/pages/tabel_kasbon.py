import streamlit as st
from db import init_db

st.title("📋 Daftar & Pengelolaan Kasbon (Anggota 3)")

if 'debts' not in st.session_state:
    st.session_state.debts = []

search = st.text_input("Cari nama pelanggan...")

filtered = st.session_state.debts
if search:
    filtered = [d for d in filtered if search.lower() in d['customerName'].lower()]

if filtered:
    for debt in filtered:
        col_a, col_b, col_c, col_d = st.columns([2, 2, 1, 1])
        with col_a:
            st.write(f"**{debt['customerName']}**")
            st.caption(f"Barang: {debt['items']}")
        with col_b:
            st.write(f"Rp {debt['totalDebt']:,.0f}")
            st.caption(f"Jatuh Tempo: {debt['dueDate']}")
        with col_c:
            if debt['status'] == 'Lunas':
                st.success("Lunas")
            else:
                st.error("Belum Lunas")
        with col_d:
            if debt['status'] == 'Belum Lunas':
                if st.button("Lunasi", key=debt['id']):
                    debt['status'] = 'Lunas'
                    st.rerun()
        st.divider()
else:
    st.info("Tidak ada data kasbon ditemukan.")