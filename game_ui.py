import tkinter as tk
from tkinter import ttk
from tkinter import *

from dao.dao_factory import DaoFactory
from dao.game_dao import GameDao
from dao.publisher_dao import PublisherDao

gamedao = DaoFactory().get_dao('game')


def get_all_games():
    return gamedao.get_all_games()


def search_games_by_id(game_id):
    return gamedao.get_game_by_id(game_id)


def search_games_by_name(game_name):
    return gamedao.get_game_by_name(game_name)


def search_games_by_published_year(published_year):
    return gamedao.get_game_by_published_year(published_year)


def search_games_by_publisher_id(publisher_id):
    return gamedao.get_game_by_publisher_id(publisher_id)


def search_games_by_type(game_type):
    return gamedao.get_game_by_type(game_type)


def update_game(game_id, game_name, published_year, publisher_id, game_type):
    return gamedao.update_game_data(game_id, game_name, published_year, publisher_id, game_type)


def add_game(game_name, published_year, publisher_id, game_type):
    return gamedao.add_game_data(game_name, published_year, publisher_id, game_type)


def remove_game(game_id):
    return gamedao.remove_game_dava(game_id)


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


def remove_publisher(publisher_id):
    return publisherdao.remove_publisher_data(publisher_id)


root = Tk()
root.title("Game Publisher")

frame_search = Frame(root)
frame_search.grid(column=0, row=0)

label_search = Label(frame_search, text="game name:", pady=20)
label_search.grid(column=0, row=0)
gamename_search = StringVar()
gamename_search_entry = Entry(frame_search, textvariable=gamename_search)
gamename_search_entry.grid(column=1, row=0)
search_button = Button(frame_search, text="Search", width=10,
                       command=lambda: search_games_by_name(gamename_search.get()))
search_button.grid(column=2, row=0, padx=10)

label_search = Label(frame_search, text="game id:", pady=20)
label_search.grid(column=0, row=1)
gameid_search = StringVar()
gameid_search_entry = Entry(frame_search, textvariable=gameid_search)
gameid_search_entry.grid(column=1, row=1)
search_button = Button(frame_search, text="Search", width=10, command=lambda: search_games_by_id(gameid_search.get()))
search_button.grid(column=2, row=1, padx=10)

label_search = Label(frame_search, text="game type:", pady=20)
label_search.grid(column=3, row=0)
gametype_search = StringVar()
gametype_search_entry = Entry(frame_search, textvariable=gametype_search)
gametype_search_entry.grid(column=4, row=0)
search_button = Button(frame_search, text="Search", width=10,
                       command=lambda: search_games_by_type(gametype_search.get()))
search_button.grid(column=5, row=0, padx=10)

label_search = Label(frame_search, text="published year:", pady=20)
label_search.grid(column=3, row=1)
publisher_year_search = StringVar()
publisher_year_search_entry = Entry(frame_search, textvariable=publisher_year_search)
publisher_year_search_entry.grid(column=4, row=1)
search_button = Button(frame_search, text="Search", width=10,
                       command=lambda: search_games_by_published_year(publisher_year_search.get()))
search_button.grid(column=5, row=1, padx=10)

# second_frame = Frame(root)
# second_frame.grid(column=5, row=2)
# label_search = Label(frame_search, text="publisher id:", pady=20)
# label_search.grid(column=1, row=2)
# publisher_year_search = StringVar()
# publisher_year_search_entry = Entry(frame_search, textvariable=publisher_year_search)
# publisher_year_search_entry.grid(column=2, row=2)
#
# label_search = Label(frame_search, text="publisher name:", pady=20)
# label_search.grid(column=1, row=2)
# publisher_year_search = StringVar()
# publisher_year_search_entry = Entry(frame_search, textvariable=publisher_year_search)
# publisher_year_search_entry.grid(column=2, row=2)

frame_router = Frame(root)
frame_router.grid(column=0, row=4, columnspan=4, rowspan=6, padx=20, pady=20)
columns = ["Game ID", "Game Name", "Year", "Type", "Publisher ID"]
game_tree = ttk.Treeview(frame_router, columns=columns, show="headings")
# tree.column("Game ID", width=40)
for column in columns[0:]:
    game_tree.column(column, width=120)
    game_tree.heading(column, text=column)
# tree.bind("<TreeviewSelect>", select_router)
game_tree.pack(side=LEFT, fill="y")
scrollbar = Scrollbar(frame_router, orient="vertical", command=game_tree.yview)
scrollbar.pack(side=RIGHT, fill="y")
game_tree.configure(yscrollcommand=scrollbar.set)

frame_buttons = Frame(root)
frame_buttons.grid(column=0, row=3)
add_button = Button(frame_buttons, text="Add", width=10)
add_button.grid(column=0, row=0, padx=5)
remove_button = Button(frame_buttons, text="Remove", width=10)
remove_button.grid(column=1, row=0, padx=5)
update_button = Button(frame_buttons, text="Update", width=10)
update_button.grid(column=2, row=0, padx=5)

# search_button = Button(frame_buttons, text="Search", width=10)
# search_button.grid(column=4, row=0, padx=30)

# add_button = Button(frame_buttons, text="Add", width=10, command=add_data)
# remove_button = Button(frame_buttons, text="Remove", width=10, command=remove_data)
# update_button = Button(frame_buttons, text="Update", width=10, command=update_data)

# frame_router2 = Frame(root)
# frame_router2.grid(column=0, row=4, columnspan=4, rowspan=6, padx=20, pady=20)
# columns = ["Publisher Name"]
# tree = ttk.Treeview(frame_router, columns=columns, show="headings")
# tree.column("Publisher Name", width=120)
# tree.heading("Publisher Name", text="Publisher Name")
# tree.pack(side=LEFT, fill="y")
# scrollbar = Scrollbar(frame_router, orient="vertical", command=tree.yview)
# scrollbar.pack(side=RIGHT, fill="y")
# tree.configure(yscrollcommand=scrollbar.set)


root.mainloop()
