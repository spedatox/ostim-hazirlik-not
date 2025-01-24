import streamlit as st

# Streamlit arayüzü başlığı
st.title("Dönem Sonu Not Hesaplama Aracı")

# Sabit ağırlıklar
VIZE_AGIRLIK = 0.25
FINAL_AGIRLIK = 0.30
ODEV_AGIRLIK = 0.10
PROJE_AGIRLIK = 0.20
KATILIM_AGIRLIK = 0.15

# Kullanıcıdan notları al
st.header("Notları Girin")

vize_not = st.number_input("Vize Notu (0-100 arası)", min_value=0.0, max_value=100.0, value=0.0)
final_not = st.number_input("Final Notu (0-100 arası)", min_value=0.0, max_value=100.0, value=0.0)
odev_not = st.number_input("Online Ödev Notu (0-100 arası)", min_value=0.0, max_value=100.0, value=0.0)
proje_not = st.number_input("Proje Notu (0-100 arası)", min_value=0.0, max_value=100.0, value=0.0)
katilim_not = st.number_input("Derse Katılım Notu (0-100 arası)", min_value=0.0, max_value=100.0, value=0.0)

# Hesaplama butonu
if st.button("Hesapla"):
    # Ağırlıklı notları hesapla
    vize_agirlikli = vize_not * VIZE_AGIRLIK
    final_agirlikli = final_not * FINAL_AGIRLIK
    odev_agirlikli = odev_not * ODEV_AGIRLIK
    proje_agirlikli = proje_not * PROJE_AGIRLIK
    katilim_agirlikli = katilim_not * KATILIM_AGIRLIK

    # Toplam notu hesapla
    toplam_not = (
        vize_agirlikli + final_agirlikli + odev_agirlikli + proje_agirlikli + katilim_agirlikli
    )

    # Sonucu göster
    st.success(f"Dönem Sonu Notunuz: {toplam_not:.2f}")
