import streamlit as st
import pandas as pd

st.title("📑 Laporan Rekapitulasi & Pengingat (Anggota 4)")

if 'debts' not in st.session_state:
    st.session_state.debts = []

df = pd.DataFrame(st.session_state.debts)

if not df.empty:
    st.subheader("Tabel Rekapitulasi Piutang")
    st.dataframe(df[['id', 'customerName', 'totalDebt', 'dueDate', 'status']], use_container_width=True)
    
    st.markdown("---")
    st.subheader("Simulasi Pengingat Tagihan WhatsApp")
    
    pelanggan_aktif = [d['customerName'] for d in st.session_state.debts if d['status'] == 'Belum Lunas']
    
    if pelanggan_aktif:
        selected_name = st.selectbox("Pilih Pelanggan untuk Dikirimi Pesan", pelanggan_aktif)
        target = next(d for d in st.session_state.debts if d['customerName'] == selected_name)
        pesan_wa = f"Halo {target['customerName']}, mengingatkan tagihan kasbon di warung sebesar Rp {target['totalDebt']:,} jatuh tempo pada {target['dueDate']}. Terima kasih!"
        st.text_area("Preview Pesan WhatsApp:", value=pesan_wa)
    else:
        st.info("Semua kasbon sudah lunas!")
else:
    st.info("Belum ada data laporan.")