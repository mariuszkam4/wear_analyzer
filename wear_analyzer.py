import os
import pandas as pd
import matplotlib.pyplot as plt

print()
print("Data processing..")
print()

# Directory path
user_directory = input ("Enter the path to the directory with the data for analysis:")
dir_path = f"{user_directory}"

# Path to the results file
results_file_path = os.path.join(dir_path, 'results.csv')

# Creating a list of files from a directory
files = [f for f in os.listdir(dir_path) if f.endswith('.csv') and f != 'results.csv']

# Presenting available parameters to the user
available_parameters = ["Długość", "Maksymalna głębokość", "Pole otworu", "Maksymalna wysokość", "Obszar szczytu"]

print("Available parameters:")
for idx, param in enumerate(available_parameters, 1):
    print(f"{idx}. {param}")

# Allowing the user to select a parameter
chosen_param_idx = int(input("Select the number of the parameter you want to process: ")) - 1
chosen_param = available_parameters[chosen_param_idx]

print(f"Parameter processing: {chosen_param}")

results = pd.DataFrame()

# Loop through the files
for file in files:
    filepath = os.path.join(dir_path, file)
    df = pd.read_csv(filepath, sep=';', skiprows=3)

    # Extraction of data on the selected parameter by the user
    param_data = df.loc[df['Name'] == chosen_param].copy()

    # Checking if the values in the 'Value' column are strings, if so they will be converted to floating point numbers
    if param_data['Value'].dtype == 'O': 
        param_data['Value'] = param_data['Value'].str.replace(',', '.').astype(float)

    # Adding a column to the DataFrame of results
    results[file] = param_data['Value']

# Adding a row with average values
results.loc['Mean'] = results.mean()

# Adding a row with standard deviation values
results.loc['Std Dev'] = results.std()

# Saving the results to a csv file
results.to_csv(results_file_path)
print("Dane zostały przetworzone. \nWyniki zapisano do pliku.")
print()

print("Creating a chart...")
data_to_plot = results.drop(['Mean', 'Std Dev'])
plt.figure(figsize=(10,6))
plt.boxplot(data_to_plot, vert=True, patch_artist=True) 
plt.title('Distribution of the results')
plt.ylabel(chosen_param)
plt.xticks([i+1 for i in range(len(data_to_plot.columns))], data_to_plot.columns, rotation='vertical')
plt.show()
print()