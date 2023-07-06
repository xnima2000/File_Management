import os
import glob
import shutil
import tkinter as tk
from tkinter import messagebox

def move_files_by_suffix(path):
    # Define mapping from file extensions to categories
    categories = {
        'Image': ['.jpg', '.JPG', '.JPEG', '.png', '.PNG', '.jpeg', '.bmp', '.tiff', '.ico', '.jfif'],
        'Video': ['.mp4', '.avi', '.flv', '.mov', '.wmv'],
        'Gif': ['.gif'],
        'Docs': ['.doc', '.docx', '.pdf', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.yaml'],
        'Music': ['.mp3', '.wav', '.wma', '.m4a', '.flac'],
        'Voice': ['.ogg'],
        'Download': ['.opdownload'],
        'Program': ['.js', '.py', '.c', '.ms9', '.sol'],
        'calender': ['.ics'],
        'subtitle': ['.ogv'],
        'Compressed': ['.zip', '.rar', '.7z', '.tar', '.gz'], 
        'windows program': ['.exe'],
    }

    if not os.path.exists(path):
        return "The path does not exist."
    elif not os.listdir(path):
        return "There is no file in this directory."
    else:
        os.chdir(path)
        files = glob.glob('*.*')  # Get all files
        for file in files:  # Move files to respective directories
            suffix = os.path.splitext(file)[1]
            for category, extensions in categories.items():
                if suffix in extensions:
                    category_path = os.path.join(path, category)
                    # suffix_path = os.path.join(category_path, suffix)
                    if not os.path.exists(category_path):  # Create directory for category if it doesn't exist
                        os.makedirs(category_path)
                    # if not os.path.exists(suffix_path):  # Create directory for suffix if it doesn't exist
                    #     os.makedirs(suffix_path)
                    shutil.move(file, os.path.join(category_path, file))
                    # shutil.move(file, os.path.join(suffix_path, file))
                    break
        return "Files moved successfully."

def execute():
    path = entry.get()
    message = move_files_by_suffix(path)
    messagebox.showinfo("Result", message)

root = tk.Tk()
root.geometry('300x150')
root.title("File Organizer")

label = tk.Label(root, text="Enter path:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Organize Files", command=execute)
button.pack()

root.mainloop()

# path = "D:/test"


