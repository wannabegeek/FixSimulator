import tkinter
from tkinter.constants import *

import Theme
from Connection import Connection
from MessageLog import MessageLog
from MessageLogAdaptor import MessageLogAdaptor
from TabbedNotebook import Notebook


def demo():
    def adjustCanvas(someVariable=None):
        fontLabel["font"] = ("arial", var.get())

    theme = Theme.Theme.loadFromFile("dark.theme")

    root = tkinter.Tk()
    root.title("tkNotebook Example")
    root['bg'] = theme["Window"]['background']

    # create a toplevel menu
    menubar = tkinter.Menu(root)

    file_menu = tkinter.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Send from File", command=root.quit)
    file_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=file_menu)

    # create a pulldown menu, and add it to the menu bar
    connection_menu = tkinter.Menu(menubar, tearoff=0)
    connection_menu.add_command(label="Connect", command=root.quit)
    connection_menu.add_command(label="Disconnect", command=root.quit)
    connection_menu.add_separator()
    recent_connections_menu = tkinter.Menu(connection_menu, tearoff=0)
    connection_menu.add_cascade(label="Connect recent", menu=recent_connections_menu)
    menubar.add_cascade(label="Connection", menu=connection_menu)

    helpmenu = tkinter.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=root.quit)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # display the menu
    root.config(menu=menubar)



    note = Notebook(root, theme['Notebook'], width=800, height=600)  # Create a Note book Instance
    note.grid(row=0, column=0, sticky=S+E+W)

    adaptors = []
    for i in range(1, 5):
        connection = Connection()
        tab = note.add_tab(text=connection.name())  # Create a tab with the text "Tab One"
        tab.rowconfigure(0, weight=1)
        tab.columnconfigure(0, weight=1)

        messageLog = MessageLog(tab, theme['MessageLog'])
        messageLog.grid(row=0, column=0, sticky=S + E + W)
        adaptor = MessageLogAdaptor(connection, messageLog)
        adaptors.append(adaptor)

    note.grid_rowconfigure(0, weight=1)
    note.grid_columnconfigure(0, weight=1)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()


if __name__ == "__main__":
    demo()