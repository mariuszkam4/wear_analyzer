import os
import pandas as pd
import matplotlib.pyplot as plt

print()
print("Data processing..")
print()

# Directory path
dir_path = r'C:\Users\mariu\Desktop\Nauka\Badania\Tribo 2023\zużycie dane surowe'

# Path to the results file
results_file_path = os.path.join(dir_path, 'results.csv')

# Wylistowanie plików w katalogu
files = os.listdir(dir_path)

# Usuń plik, jeśli istnieje
if os.path.isfile(results_file_path):
    os.remove(results_file_path)

# Stworzenie pustego DataFrame do przechowywania wyników
results = pd.DataFrame()

# Pętla po plikach
for file in files:
    # Sprawdzanie, czy plik jest plikiem csv i nie jest plikiem wyników
    if file.endswith('.csv') and file != 'results.csv':
        # Tworzenie pełnej ścieżki do pliku
        filepath = os.path.join(dir_path, file)
        
        # Czytanie pliku csv
        df = pd.read_csv(filepath, sep=';', skiprows=3)

        # Wyodrębnianie danych dot. pola otworu
        pole_otworu = df.loc[df['Name']=='Pole otworu'].copy()  # Dodajemy .copy(), aby uniknąć ostrzeżenia

        # Jeżeli wartości w kolumnie 'Value' są stringami, przekonwertujmy je na liczby zmiennoprzecinkowe
        if pole_otworu['Value'].dtype == 'O':  # 'O' oznacza obiekt, czyli w tym przypadku string
            pole_otworu['Value'] = pole_otworu['Value'].str.replace(',', '.').astype(float)

        # Dodanie kolumny do DataFrame wyników
        results[file] = pole_otworu['Value']

# Dodanie wiersza z wartościami średnimi
results.loc['Mean'] = results.mean()

# Dodanie wiersza z wartościami odchylenia standardowego
results.loc['Std Dev'] = results.std()

# Zapisanie wyników do pliku csv
results.to_csv(results_file_path)

print("Dane zostały przetworzone. \nWyniki zapisano do pliku.")
print()

print("Tworzenie wykresu...")
data_to_plot = results.drop(['Mean', 'Std Dev'])
plt.figure(figsize=(10,6))
plt.boxplot(data_to_plot, vert=True, patch_artist=True) # Vert=True sprawia, że wykres jest pionowy
plt.title('Rozkład wyników')
plt.ylabel('Wartość zyżucia [μm\u00B2]')
plt.xticks([i+1 for i in range(len(data_to_plot.columns))], data_to_plot.columns, rotation='vertical')
plt.show()
print()