import pandas as pd
import matplotlib.pyplot as plt
import locale
locale.setlocale(locale.LC_TIME, 'Ukrainian_Ukraine.1251')

df=pd.read_csv("comptagevelo2011.csv")
print(df.head())
print(df.info())
print(df.describe())

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(0)
df[numeric_cols] = df[numeric_cols].astype(int)
print("\nПокращений датафрейм\n")
print(df.info())
print(df.head())

total_all_tracks = df[numeric_cols].sum().sum()
print("\nЗагальна кількість велосипедистів за рік (усі доріжки):", total_all_tracks)

total_per_track = df[numeric_cols].sum()
print("Загальна кількість велосипедистів за рік на кожній велодоріжці:")
print(total_per_track)

selected_tracks = ['Rachel / Papineau', 'Berri1', 'Maisonneuve_2']
print("\nНайпопулярніший місяць для обраних доріжок:")
month_order = {month: i for i, month in enumerate(df['Date'].dt.month_name().unique(), 1)}
for track in selected_tracks:
    monthly_sum = df.groupby(df['Date'].dt.month)[track].sum().sort_index()
    monthly_sum.index = monthly_sum.index.map(lambda x: pd.to_datetime(str(x), format='%m').strftime('%B'))
    most_popular_month = monthly_sum.idxmax()
    print(f"{track}: місяць {most_popular_month} з {monthly_sum[most_popular_month]} велосипедистами")

track_to_plot = 'Rachel / Papineau'
monthly_data = df.groupby(df['Date'].dt.month)[track_to_plot].sum().sort_index()
monthly_data.index = monthly_data.index.map(lambda x: pd.to_datetime(str(x), format='%m').strftime('%B'))
plt.figure(figsize=(10,5))
monthly_data.plot(kind='bar', color='skyblue')
plt.title(f"Завантаженість велодоріжки {track_to_plot} по місяцях")
plt.xlabel("Місяць")
plt.ylabel("Кількість велосипедистів")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

