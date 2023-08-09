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
files = [f for f in os.listdir(dir_path) if f.endswith('.csv') and f != 'results.csv']

# Prezentowanie dostępnych parametrów użytkownikowi
available_parameters = ["Długość", "Maksymalna głębokość", "Pole otworu", "Maksymalna wysokość", "Obszar szczytu"]

print("Dostępne parametry:")
for idx, param in enumerate(available_parameters, 1):
    print(f"{idx}. {param}")

# Pozwól użytkownikowi na wybór parametru
chosen_param_idx = int(input("Wybierz numer parametru, który chcesz przetworzyć: ")) - 1
chosen_param = available_parameters[chosen_param_idx]

print(f"Przetwarzanie parametru: {chosen_param}")

# Stworzenie pustego DataFrame do przechowywania wyników
results = pd.DataFrame()

# Pętla po plikach
for file in files:
    filepath = os.path.join(dir_path, file)
    df = pd.read_csv(filepath, sep=';', skiprows=3)

    # Wyodrębnianie danych dot. wybranego parametru przez użytkownika
    param_data = df.loc[df['Name'] == chosen_param].copy()

    # Jeżeli wartości w kolumnie 'Value' są stringami, przekonwertujmy je na liczby zmiennoprzecinkowe
    if param_data['Value'].dtype == 'O':  # 'O' oznacza obiekt, czyli w tym przypadku string
        param_data['Value'] = param_data['Value'].str.replace(',', '.').astype(float)

    # Dodanie kolumny do DataFrame wyników
    results[file] = param_data['Value']

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
plt.ylabel(chosen_param)
plt.xticks([i+1 for i in range(len(data_to_plot.columns))], data_to_plot.columns, rotation='vertical')
plt.show()
print()