# rumus
# Broca
# pria = berat ideal = (tinggi_cm - 100) - ((tinggi_cm - 100) * 0.10)
# wanita = berat ideal = (tinggi_cm - 100) - ((tinggi_cm - 100 * 0.15))

# BMI (Body Mass Index)
# < 18.15 "kurus"
# < 25 "ideal"
# < 30 "Kelebihan berat"
# 30+ "obesitas" 


import streamlit as st 

st.markdown("""
    <style>
    .rainbow-text {
        font-size: 40px;
        font-weight: bold;
        background: linear-gradient(
            90deg,
            red,
            orange,
            yellow,
            green,
            cyan,
            blue,
            violet
        );
        background-size: 400% 100%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: rainbow 5s linear infinite;
        text-align: center;
    }

    @keyframes rainbow {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }
    </style>
    <div class="rainbow-text">Cek Ideal Berat Badanmu</div>

            """,
        unsafe_allow_html=True
)

st.markdown("""---""")

with st.expander("Cara penggunaan"):
    st.write("""Rumus BIM (Body Mass Index)
BIM mengukur proporsi berat badan dengan tinggi badan.\n
Rumus Broca (Ideal Body Weight)
Broca menghitung berat badan ideal berdasarkan tinggi""")

with st.expander("Broca"):
    st.write("""

✅ Cara Menggunakan Rumus Broca
Ukur tinggi badan dalam cm.
Contoh: 160 cm

Gunakan rumus sesuai jenis kelamin:

Pria:
(Tinggi - 100) - 10% dari hasil
= (160 - 100) - 10% = 60 - 6 = 54 kg

Wanita:
(Tinggi - 100) - 15% dari hasil
= (160 - 100) - 15% = 60 - 9 = 51 kg

Hasil = berat badan ideal.
""")
    

with st.expander("BIM"):
    st.write("""

    ✅ Cara Menggunakan Rumus BIM
Ukur berat badan dalam kilogram (kg).
Contoh: 60 kg

Ukur tinggi badan dalam meter (m).
Contoh: 1,65 m

Masukkan ke rumus:

BIM = Berat / (Tinggi x Tinggi)
BIM = 60 / (1,65 x 1,65) = 22,04
Lihat kategori berat badan:

< 18,5 = Kurus

18,5–24,9 = Normal

25–29,9 = Gemuk

≥ 30 = Obesitas

""")

#Rumus Broca

st.markdown("""---""")

st.markdown("<h3 style='text-align: center;'>Broca (Ideal Body Weight)</h3>", unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .stRadio > div {
        display: flex;
        justify-content: center;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

st.markdown("<h5 style='text-align: center;'>Masukkan Jenis Kelamin anda</h5>", unsafe_allow_html=True)

gender = st.radio("",
    ["Laki - Laki", "Perempuan"],
    horizontal=True
)

Pria = 0.10
Wanita = 0.15

if gender == "Laki - Laki":
    Ngender = 0.10
else:
    Ngender = 0.15

st.markdown("<h5 style='text-align: center;'>Masukkan tinggi badan anda</h5>", unsafe_allow_html=True)
Tinggi_Broca = st.number_input(" ", value=None, placeholder="Masukkan tinggi badan mu minimal 150 ke atas, maksimal 200")

if st.button("Cek Broca", icon="✅", key="Broca"):
    if Tinggi_Broca:
        if Tinggi_Broca <= 150:
            st.warning("Masukkan Tinggi Badan Anda Minimal 150 Ke Atas")
        elif  Tinggi_Broca >= 210:
            st.warning("Emang tinggi badan lu di atas 200cm?")
        else:
            Tinggi_Broca = int(Tinggi_Broca)
            Hasil = (Tinggi_Broca - 100) - ((Tinggi_Broca - 100) * Ngender)
            st.markdown("<h5 style='text-align: center;'>Hasil</h5>", unsafe_allow_html=True)
            st.write(f"""
                    Jenis Kelamin   : {gender}\n
                    Tinggi badan    : {Tinggi_Broca}cm\n
                    Hasil           : {Hasil} Kg""")
            st.success(f"Berat badan idealmu sekitar {Hasil} Kg")
    else:
        st.warning("Masukkan Angka Terlebih Dahulu", icon="⚠️")

st.markdown("---")

# Rumus BIM

st.markdown("<h3 style='text-align: center;'>BIM (Body Mass Index)</h3>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center;'>Masukkan tinggi badan anda</h5>", unsafe_allow_html=True)
tinggi_bim_m = st.number_input("", value=None, placeholder="Masukkan tinggi badan anda minimal 100, maksimal 200")
st.markdown("<h5 style='text-align: center;'>Masukkan berat badan anda</h5>", unsafe_allow_html=True)
berat_bim = st.number_input("", value=None, placeholder="Masukkan berat badan anda")
if st.button("Cek BIM", icon="✅", key="BIM"):
    if tinggi_bim_m:
        if tinggi_bim_m <= 100:
            st.warning("Masukkan tinggi badan lebih dari 100cm", icon="⚠️")        
    else:
        st.warning("Masukkan tinggi badan terlebih dahulu", icon="⚠️")
    if berat_bim == None:
        st.warning("Masukkan berat badan terlebih dahulu", icon="⚠️")
    if tinggi_bim_m and berat_bim:
        tinggi_bim = tinggi_bim_m / 100
        berat_bim = int(berat_bim)
        bim = berat_bim / tinggi_bim ** 2
        if bim < 18.5:
            hasil = "Kurus"
        elif 18.5 <= bim < 25:
            hasil = "Ideal"
        elif 25 <= bim < 30:
            hasil = "Gemuk"
        else:
            hasil = "Obesitas"
        
        st.markdown("<h5 style='text-align: center;'>Hasil</h5>", unsafe_allow_html=True)
        st.write(f"""
            Tinggi Badan Anda        : {tinggi_bim_m}\n
            Berat Badan Anda         : {berat_bim}\n
            Hasil Kondisi Badan Anda : {hasil}
        """)
        st.success(f"Kondisi Badanmu Sekarang : {hasil}")

# COPYRIGHT

st.markdown("---")
st.markdown("""
    <div style="text-align: center; font-size: 25px; color: #555;">
        <p>Follow us on:</p>
        <a href="https://github.com" target="https://github.com/Moelmo" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/128/5968/5968866.png" width="35" height="35" alt="GitHub" />
        </a>
        <a href="https://discord.com" target="https://discord.users/" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/128/2111/2111370.png" width="35" height="35" alt="Discord" />
        </a>
        <a href="https://www.tiktok.com" target="https://tiktok.com/@moelmo57" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/128/4782/4782345.png" width="35" height="35" alt="TikTok" />
        </a>
        <a href="https://www.instagram.com" target="https://instagram.com/moelmo.57" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/128/2111/2111463.png" width="35" height="35" alt="Instagram" />
        </a>
    </div>
    """, unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 25px; color: #888;'>© Moelmo 2025</p>", unsafe_allow_html=True)