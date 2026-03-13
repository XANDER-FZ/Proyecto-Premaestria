import data_loader
import CLI
import processor

if __name__ == "__main__":
    file_path = "data/estudiantes.csv"
    if processor.verify_csv_extension(file_path):
        data = data_loader.extrac_data(file_path)
        CLI.CLI_window(data)