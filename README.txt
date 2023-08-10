Wear analyzer

EN
The script is used to analyze .csv files containing the results of surface profile analysis. The files are generated on the basis of analyses performed in TalyMap Platinum 7.4 software. As a result of comparative studies of various materials, a number of files with measurement data of individual samples are obtained. It is then necessary to extract the data of interest from the files and make comparisons between them. The program allows automatic processing of the files in the indicated location. The user can select the parameter of interest from those indicated in the script, viz: "Length", "Maximum depth", "Hole area", "Maximum depth", "Peak area". After selecting the paramter, the script will make successive iterations through the files in the indicated directory and extract the indicated paramters. It will then save them in the results.csv file in separate columns for each sample. The column name will be the name of the source data file. The script will automatically count the mean and standard deviation for each data series. Finally, it will display a box-and-whisker plot showing the distribution of results in each data file.

To perform the analysis, you need to:
- run the wear_analyzer.py script using the python interpreter,
- point to the path to the directory where the files for analysis are located,
- indicate the parameter of interest,
- when the script finishes, the results.csv file should be automatically created in the directory where the files to be analyzed are located, and the box-sniff chart should be displayed.

Attention. 
1) For the script to work properly, the indicated folder should contain only the files to be analyzed.
2) When entering the folder path, do not use quotation marks.


PL
Skrypt służy do analizy plików .csv zawierających wyniki analizy profili powierzchni. Pliki genereowane są na podstawie analiz przeprowadzonych w oprogramowaniu TalyMap Platinum 7.4. W wyniku prowadzenia badań porównawczych różnych materiałów uzyskuje się szereg plików z danymi pomiarowymi poszczególnych próbek. Następnie należy pobrać z plików interesujące nas dane i dokonać ich porównania. Program pozwala na automatyczne przetworzenie plików we wskazanej lokalizacji. Użytkownik ma możliwość wyboru interesującego go parametru spośród wskazanych w skrypcie tj.: "Długość", "Maksymalna głębokość", "Pole otworu", "Maksymalna głębokość", "Obszar szczytu". Po wyborze paramteru skrypt dokona kolejnych iteracji poprzez pliki znajdujące się we wskazanym katalogu i wyodrębni wskazane paramtery. Nastepnie zapisze je w pliku results.csv w osobnych kolumanch dla poszczególnych próbek. Nazwą kolumny będzie nazwa źródłowego pliku danych. Skrypt automatycznie policzy średnią oraz odchylenie standardowe dla poszczególnych serii danych. Na koniec wyświetli wykres ramka-wąsy prezentujący rozkład wyników w poszczególnych plikach danych.

W celu przeprowadzenia analizy należy:
- uruchomić skrypt wear_analyzer.py za pomocą interpretera pythona,
- wskazać ścieżkę do katalogu w którym znajdują się pliki do analizy,
- wskazać interesujący nas parametr,
- po zakończeniu skryptu plik results.csv powinien zostać automatycznie utworzony w katalogu w którym znajdują się analizowane pliki oraz powinien wyświetlić się wykres skrzynka-wąsy.

Uwaga. 
1. W celu prawidłowego działania skryptu, we wskazanym folderze powinny znajdować się wyłącznie pliki poddawane analizie.
2. Wproawdzając ścieżkę dostępu do folderu nie używaj cudzysłowu.