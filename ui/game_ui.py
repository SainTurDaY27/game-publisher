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


def add_game(game_name, published_year, game_type, publisher_id):
    return gamedao.add_game_data(game_name, published_year, game_type, publisher_id)


def remove_game_by_id(game_id):
    return gamedao.remove_game_dava(game_id)


def remove_game_by_name(game_name):
    return gamedao.remove_game_dava(game_name)


root = Tk()
root.title("Game Data")

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

label_search = Label(frame_search, text="publisher id:", pady=20)
label_search.grid(column=0, row=2)
publisher_id_search = StringVar()
publisher_id_search_entry = Entry(frame_search, textvariable=publisher_id_search)
publisher_id_search_entry.grid(column=1, row=2)
search_button = Button(frame_search, text="Search", width=10,
                       command=lambda: search_games_by_publisher_id(publisher_id_search.get()))
search_button.grid(column=2, row=2, padx=10)

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
remove_id_button = Button(frame_buttons, text="Remove using ID", width=20, command=lambda: remove_game_by_id(gameid_search.get()))
remove_id_button.grid(column=1, row=0, padx=5)
remove_name_button = Button(frame_buttons, text="Remove using Name", width=20, command=lambda: remove_game_by_name(gamename_search.get()))
remove_name_button.grid(column=2, row=0, padx=5)
update_button = Button(frame_buttons, text="Update", width=10, command=lambda: update_game(gameid_search.get(), gamename_search.get(), publisher_year_search.get(), gametype_search.get(), publisher_id_search.get()))
update_button.grid(column=3, row=0, padx=5)


root.mainloop()
