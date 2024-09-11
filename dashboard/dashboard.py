import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Menambahkan judul dan deskripsi di sidebar
st.sidebar.image('bikerent.jpg', use_column_width=True)

st.sidebar.header("Identitas Saya")
st.sidebar.write("Nama: Mohammad Hikam")
st.sidebar.write("Email: muhamadhikam94@gmail.com")

# Load data
day_df = pd.read_csv('day_cleaned.csv')
hour_df = pd.read_csv('hour_cleaned.csv')

st.title("Analisis Penyewaan Sepeda")

st.subheader("1. Musim Apa Dengan Pelanggan Penyewa Sepeda Terbanyak?")

colors = ["#FF6347", "#4682B4", "#32CD32", "#FFD700"]

# Plot bar untuk penyewaan per musim
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    y="count", 
    x="season",
    data=day_df.sort_values(by="season", ascending=False),
    palette=colors,
    ax=ax,
    edgecolor='black',
    linewidth=1
)
ax.set_title("Grafik Penyewaan Sepeda Tiap Musim", fontsize=20)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=10)

st.pyplot(fig)

season_data = day_df.groupby(by='season').agg({
    'count': 'sum'
}).reset_index()

season_data.columns = ['season', 'total_count']

max_count = season_data['total_count'].max()
max_season = season_data.loc[season_data['total_count'].idxmax(), 'season']

season_mapping = {
    1: 'Spring',
    2: 'Summer',
    3: 'Fall',
    4: 'Winter'
}

max_season_name = season_mapping.get(max_season, 'Unknown')

st.write(f"Total penyewaan tertinggi adalah {max_count} pada musim {max_season_name}.")

st.subheader("2. Pada Jam Berapa Total Penyewaan Sepeda Tertinggi Terjadi?")

hourly_data = hour_df.groupby(by='hour').agg({
    'count': 'sum'
}).reset_index()

hourly_data.columns = ['hour', 'count_sum']

# Plot line untuk penyewaan per jam
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(hourly_data['hour'], hourly_data['count_sum'], color='skyblue', marker='o')
ax.set_title('Total Count per Hour', fontsize=16)
ax.set_xlabel('Hour', fontsize=14)
ax.set_ylabel('Count', fontsize=14)
ax.grid(True, axis='x', linestyle='--', linewidth=1)
plt.xticks(ticks=hourly_data['hour'], labels=hourly_data['hour'])

st.pyplot(fig)

max_count = hourly_data['count_sum'].max()
max_hour = hourly_data.loc[hourly_data['count_sum'].idxmax(), 'hour']

st.write(f"Total penyewaan sepeda tertinggi adalah {max_count} pada jam {max_hour}.")

st.header("Kesimpulan")

st.subheader("Pertanyaan 1: Musim Apa Dengan Pelanggan Penyewa Sepeda Terbanyak?")
st.write("""
Dari analisis data penyewaan sepeda berdasarkan musim, musim dengan jumlah pelanggan 
penyewa sepeda terbanyak adalah Musim Fall (Musim Gugur). Pada musim ini, jumlah total 
penyewaan sepeda mencapai angka tertinggi, yaitu 1,061,129 unit. Musim gugur menunjukkan puncak 
aktivitas penyewaan sepeda yang signifikan, kemungkinan karena cuaca yang masih nyaman untuk bersepeda
dan berbagai acara outdoor yang sering diadakan pada musim ini.
""")

st.subheader("Pertanyaan 2: Pada Jam Berapa Total Penyewaan Sepeda Tertinggi Terjadi?")
st.write("""
Berdasarkan analisis data penyewaan sepeda per jam, total penyewaan sepeda tertinggi 
terjadi pada jam 17. Pada jam ini, jumlah penyewaan sepeda mencapai nilai maksimum 
sebesar 336,860 unit. Temuan ini menunjukkan bahwa waktu sore, terutama jam-jam 
menjelang akhir hari kerja, adalah periode puncak untuk penyewaan sepeda. 
Ini mungkin disebabkan oleh tingginya permintaan sepeda sebagai sarana transportasi 
pulang kerja atau untuk aktivitas rekreasi sore hari.
""")