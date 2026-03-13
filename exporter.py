import json

def export_JSON(file_export):
    with open("data/reporte.json", "w", encoding="utf-8") as file:
        json.dump(file_export, file, ensure_ascii=False, indent=4)