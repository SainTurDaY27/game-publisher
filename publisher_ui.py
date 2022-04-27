from tkinter import ttk
from tkinter import *

from dao.dao_factory import DaoFactory

publisherdao = DaoFactory().get_dao('publisher')


def get_all_publishers():
    return publisherdao.get_all_publishers()


def search_publishers_by_id(publisher_id):
    return publisherdao.get_publisher_by_id(publisher_id)


def search_publishers_by_name(publisher_name):
    return publisherdao.get_publisher_by_name(publisher_name)


def update_publisher(publisher_id, publisher_name):
    return publisherdao.update_publisher_data(publisher_id, publisher_name)


def add_publisher(publisher_name):
    return publisherdao.add_publisher_data(publisher_name)


def remove_publisher_by_id(publisher_id):
    return publisherdao.remove_publisher_by_id(publisher_id)


def remove_publisher_by_name(publisher_name):
    return publisherdao.remove_publisher_by_name(publisher_name)


root = Tk()
root.title("Game Publisher")

frame_search = Frame(root)
frame_search.grid(column=0, row=0)

label_search = Label(frame_search, text="publisher ID:", pady=20)
label_search.grid(column=0, row=0)
publishername_search = StringVar()
publishername_search_entry = Entry(frame_search, textvariable=publishername_search)
publishername_search_entry.grid(column=1, row=0)
search_button = Button(frame_search, text="Search", width=10,
                       command=lambda: search_publishers_by_id(publishername_search.get()))
search_button.grid(column=2, row=0, padx=10)

label_search = Label(frame_search, text="publisher_name:", pady=20)
label_search.grid(column=0, row=1)
publisherid_search = StringVar()
publisherid_search_entry = Entry(frame_search, textvariable=publisherid_search)
publisherid_search_entry.grid(column=1, row=1)
search_button = Button(frame_search, text="Search", width=10,
                       command=lambda: search_publishers_by_name(publisherid_search.get()))
search_button.grid(column=2, row=1, padx=10)

frame_router = Frame(root)
frame_router.grid(column=0, row=4, columnspan=4, rowspan=6, padx=20, pady=20)
columns = ["Publisher ID", "Publisher Name"]
publisher_tree = ttk.Treeview(frame_router, columns=columns, show="headings")
for column in columns[0:]:
    publisher_tree.column(column, width=120)
    publisher_tree.heading(column, text=column)
publisher_tree.pack(side=LEFT, fill="y")
scrollbar = Scrollbar(frame_router, orient="vertical", command=publisher_tree.yview)
scrollbar.pack(side=RIGHT, fill="y")
publisher_tree.configure(yscrollcommand=scrollbar.set)

frame_buttons = Frame(root)
frame_buttons.grid(column=0, row=3)
add_button = Button(frame_buttons, text="Add", width=10, command=lambda: add_publisher(publishername_search.get()))
add_button.grid(column=0, row=0, padx=5)
remove_id_button = Button(frame_buttons, text="Remove using id", width=20, command=lambda: remove_publisher_by_id(publisherid_search.get()))
remove_id_button.grid(column=1, row=0, padx=5)
remove_name_button = Button(frame_buttons, text="Remove using name", width=20, command=lambda: remove_publisher_by_name(publishername_search.get()))
remove_name_button.grid(column=2, row=0, padx=5)
update_button = Button(frame_buttons, text="Update", width=10, command=lambda: update_publisher(publisherid_search.get(), publishername_search.get()))
update_button.grid(column=3, row=0, padx=5)

root.mainloop()
