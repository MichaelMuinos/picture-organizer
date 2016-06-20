import time
import os
import tkinter as tk
import shutil

directory_path = "E:\\My Digital Camera Pictures\\"
picture_directory_path = "I:\\DCIM\\100MSDCF\\"


class StorePictures(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("File")
        self.label = tk.Label(self, text="Name")
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Done", command=self.on_button)
        self.label.pack(side=tk.LEFT)
        self.button.pack(side=tk.BOTTOM)
        self.entry.pack(side=tk.RIGHT)

    def on_button(self):
        pictures = os.listdir(picture_directory_path)

        date_string = get_date_string(pictures[0]) + self.entry.get() + "\\"
        path = get_year_directory_path(directory_path)
        path = get_year_and_date_directory_path(path, date_string)

        count = get_number_of_jpg(pictures)

        index = 0
        for picture in pictures:
            filename, file_extension = os.path.splitext(picture_directory_path + picture)
            if file_extension == ".JPG":
                index += 1
                picture_date_created = get_date_string(picture) + self.entry.get() + " #"
                temp_picture_name = picture_date_created + str(index) + " of " + str(count) + ".JPG"
                picture_directory = path + temp_picture_name
                shutil.copy(picture_directory_path + picture, picture_directory)

        self.quit()


def get_year_directory_path(path):
    temp_directory = path + "20" + time.strftime("%y") + " Pictures\\"
    if not os.path.exists(temp_directory):
        os.makedirs(temp_directory)
    path = temp_directory
    return path


def get_year_and_date_directory_path(path, date_string):
    temp_directory = path + date_string
    if not os.path.exists(temp_directory):
        os.makedirs(temp_directory)
    path = temp_directory
    return path


def get_date_string(picture):
    return "20" + time.strftime("%y") + " - " + time.strftime("%m-%d-%y", time.localtime(os.path.getctime(picture_directory_path + picture))) + " - "


def get_number_of_jpg(pictures):
    count = 0;
    for picture in pictures:
        filename, file_extension = os.path.splitext(picture_directory_path + picture)
        if file_extension == ".JPG":
            count += 1
    return count

app = StorePictures()
app.mainloop()