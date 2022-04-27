from tkinter import ttk, messagebox
from tkinter import *

from dao.dao_factory import DaoFactory

gamedao = DaoFactory().get_dao('game')


def get_all_games():
    return gamedao.get_all_games()


def check_data(data):
    if data is not None:
        if isinstance(data, list):
            for game in data:
                game_tree.insert('', 'end', values=(
                    game.id, game.game_name, game.published_year, game.game_type, game.publisher_id))
        else:
            game_tree.insert('', 'end', values=(
                data.id, data.game_name, data.published_year, data.game_type,
                data.publisher_id))
    else:
        messagebox.showinfo("Error", "No game found")
        refresh_game_tree()


def search_games_by_id(game_id):
    game_tree.delete(*game_tree.get_children())
    game_data = gamedao.get_game_by_id(game_id)
    check_data(game_data)
    # if game_data is not None:
    #     game_tree.insert('', 'end', values=(
    #         game_data.id, game_data.game_name, game_data.published_year, game_data.game_type, game_data.publisher_id))
    # else:
    #     messagebox.showinfo("Error", "No game found")
    #     refresh_game_tree()


def search_games_by_name(game_name):
    game_tree.delete(*game_tree.get_children())
    game_data = gamedao.get_game_by_name(game_name)
    check_data(game_data)
    # if game_data is not None:
    #     game_tree.insert('', 'end', values=(
    #         game_data.id, game_data.game_name, game_data.published_year, game_data.game_type, game_data.publisher_id))
    # else:
    #     messagebox.showinfo("Error", "No game found")
    #     refresh_game_tree()


def search_games_by_published_year(published_year):
    game_tree.delete(*game_tree.get_children())
    game_data = gamedao.get_game_by_published_year(published_year)
    check_data(game_data)
    # if game_data is not None:
    #     if isinstance(game_data, list):
    #         for game in game_data:
    #             game_tree.insert('', 'end', values=(
    #                 game.id, game.game_name, game.published_year, game.game_type, game.publisher_id))
    #     else:
    #         game_tree.insert('', 'end', values=(
    #             game_data.id, game_data.game_name, game_data.published_year, game_data.game_type,
    #             game_data.publisher_id))
    # else:
    #     messagebox.showinfo("Error", "No game found")
    #     refresh_game_tree()


def search_games_by_publisher_id(publisher_id):
    game_tree.delete(*game_tree.get_children())
    game_data = gamedao.get_game_by_publisher_id(publisher_id)
    check_data(game_data)
    # if game_data is not None:
    #     if isinstance(game_data, list):
    #         for game in game_data:
    #             game_tree.insert('', 'end', values=(
    #                 game.id, game.game_name, game.published_year, game.game_type, game.publisher_id))
    #     elif isinstance(game_data, model.GameData):
    #         game_tree.insert('', 'end', values=(
    #             game_data.id, game_data.game_name, game_data.published_year, game_data.game_type,
    #             game_data.publisher_id))
    # else:
    #     messagebox.showinfo("Error", "No game found")
    #     refresh_game_tree()


def search_games_by_type(game_type):
    game_tree.delete(*game_tree.get_children())
    game_data = gamedao.get_game_by_type(game_type)
    check_data(game_data)
    # if game_data is not None:
    #     if isinstance(game_data, list):
    #         for game in game_data:
    #             game_tree.insert('', 'end', values=(
    #                 game.id, game.game_name, game.published_year, game.game_type, game.publisher_id))
    #     else:
    #         game_tree.insert('', 'end', values=(
    #             game_data.id, game_data.game_name, game_data.published_year, game_data.game_type,
    #             game_data.publisher_id))
    # else:
    #     messagebox.showinfo("Error", "No game found")
    #     refresh_game_tree()


def update_game(game_id, game_name, published_year, publisher_id, game_type):
    gamedao.update_game_data(game_id, game_name, published_year, publisher_id, game_type)
    refresh_game_tree()


def add_game(game_name, published_year, game_type, publisher_id):
    gamedao.add_game_data(game_name, published_year, game_type, publisher_id)
    refresh_game_tree()


def remove_game_by_id(game_id):
    gamedao.remove_game_data_by_id(game_id)
    refresh_game_tree()


def remove_game_by_name(game_name):
    gamedao.remove_game_data_by_name(game_name)
    refresh_game_tree()


def refresh_game_tree():
    game_tree.delete(*game_tree.get_children())
    for game in get_all_games():
        game_tree.insert('', 'end',
                         values=(game.id, game.game_name, game.published_year, game.game_type, game.publisher_id))


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
game_tree.column("Game ID", width=55)
game_tree.heading("Game ID", text="Game ID")
game_tree.column("Game Name", width=250)
game_tree.heading("Game Name", text="Game Name")
game_tree.column("Year", width=50)
game_tree.heading("Year", text="Year")
game_tree.column("Type", width=100)
game_tree.heading("Type", text="Type")
game_tree.column("Publisher ID", width=100)
game_tree.heading("Publisher ID", text="Publisher ID")

game_tree.pack(side=LEFT, fill="y")
scrollbar = Scrollbar(frame_router, orient="vertical", command=game_tree.yview)
scrollbar.pack(side=RIGHT, fill="y")
game_tree.configure(yscrollcommand=scrollbar.set)

game_data = get_all_games()
for game in game_data:
    game_tree.insert("", END, values=(game.id, game.game_name, game.published_year, game.game_type, game.publisher_id))

frame_buttons = Frame(root)
frame_buttons.grid(column=0, row=3)
add_button = Button(frame_buttons, text="Add", width=10, command=lambda: add_game(gamename_search.get(),
                                                   publisher_year_search.get(), gametype_search.get(),
                                                   publisher_id_search.get()))
add_button.grid(column=0, row=0, padx=5)
remove_id_button = Button(frame_buttons, text="Remove using Game ID", width=20,
                          command=lambda: remove_game_by_id(gameid_search.get()))
remove_id_button.grid(column=1, row=0, padx=5)
remove_name_button = Button(frame_buttons, text="Remove using Name", width=20,
                            command=lambda: remove_game_by_name(gamename_search.get()))
remove_name_button.grid(column=2, row=0, padx=5)
update_button = Button(frame_buttons, text="Update", width=10,
                       command=lambda: update_game(gameid_search.get(), gamename_search.get(),
                                                   publisher_year_search.get(), gametype_search.get(),
                                                   publisher_id_search.get()))
update_button.grid(column=3, row=0, padx=5)

bottom_frame = Frame(root)
bottom_frame.grid(column=0, row=10, columnspan=4, rowspan=2)
refresh_button = Button(bottom_frame, text="Refresh", width=10, command=lambda: refresh_game_tree())
refresh_button.grid(column=0, row=0, padx=5)

root.mainloop()
