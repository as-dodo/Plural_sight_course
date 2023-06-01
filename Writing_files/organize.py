import os
import shutil

# Путь к рабочему столу
desktop_path = os.path.expanduser("~/Desktop/test_folder")


folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".doc", ".docx", ".txt", ".pdf"],
    "Archives": [".zip", ".rar"]
}
# Создаем папки назначения, если они не существуют
for folder_name in folders:
    folder_path = os.path.join(desktop_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Организуем файлы по папкам
for file_name in os.listdir(desktop_path):
    original_file_path = os.path.join(desktop_path, file_name)
    if os.path.isfile(original_file_path):
        for folder_name, extentions in folders.items():
            for extention in extentions:
                if file_name.endswith(extention):
                    destination_folder = os.path.join(desktop_path, folder_name)
                    shutil.move(original_file_path, destination_folder)

