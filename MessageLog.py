import tkinter
from tkinter.constants import *
from tkinter.ttk import Style

import Theme


class MessageLog(tkinter.Frame):
    """Notebook Widget"""

    def __init__(self, parent, theme, **kw):
        m = tkinter.PanedWindow(parent, orient=HORIZONTAL, relief='flat', borderwidth=0)
        m['bg'] = "red"
        m.grid(sticky=N+E+S+W)

        leftframe = tkinter.Frame(m, relief='flat', borderwidth=1)
        leftframe['bg'] = theme["SummaryPane"]["background"]

        scrollbar = tkinter.Scrollbar(leftframe, orient=VERTICAL, relief='flat')

        var = tkinter.IntVar()
        control = tkinter.Frame(leftframe, relief='flat', borderwidth=1)
        control['bg'] = theme["SummaryPane"]["background"]
        button = tkinter.Button(control, text="connect", background=theme["SummaryPane"]["background"], activebackground=theme["SummaryPane"]["background"])
        button.grid(row=0, column=0, sticky=W)
        c = tkinter.Checkbutton(control, text="Show Admin Messages", variable=var, background=theme["SummaryPane"]["background"], foreground=theme["SummaryPane"]["textColor"])
        c.grid(row=0, column=1, sticky=E)
        control.grid(columnspan=2)
        control.rowconfigure(0, weight=1)
        control.columnconfigure(0, weight=1)

        control.grid(sticky=N+E+W)
        self.listbox = tkinter.Listbox(leftframe,
                                  yscrollcommand=scrollbar.set,
                                  relief='flat',
                                  selectmode=SINGLE,
                                  foreground=theme["SummaryPane"]["textColor"],
                                  background=theme["SummaryPane"]["background"],
                                  selectbackground=theme["SummaryPane"]["selectedMessageBackground"],
                                  selectforeground=theme["SummaryPane"]["selectedTextColor"])

        self.listbox.bind('<<ListboxSelect>>', self.onselect)

        scrollbar.config(command=self.listbox.yview)
        scrollbar.grid(row=1, column=1, sticky=N+E+S)
        # scrollbar.pack(side=RIGHT, fill=Y)
        # self.listbox.pack(side=LEFT, fill=BOTH, expand=1)
        self.listbox.grid(row=1, column=0, sticky=N+E+S+W)
        leftframe.rowconfigure(1, weight=1)
        leftframe.columnconfigure(0, weight=1)

        # listbox.insert(END, "a list entry")
        # for item in range(1, 100):
        #     listbox.insert(END, str(item))

        # top = tkinter.Label(leftframe, text="top pane")
        # top['fg'] = theme["SummaryPane"]["textColor"]
        # top.pack()
        m.add(leftframe, stretch="always", minsize=200)

        rightframe = tkinter.Frame(m, relief='flat', borderwidth=1)
        rightframe['bg'] = theme["DetailPane"]["background"]
        bottom = tkinter.Label(rightframe, text="bottom pane")
        bottom['fg'] = theme["DetailPane"]["textColor"]
        bottom['bg'] = theme["DetailPane"]["background"]
        bottom.pack()
        # rightframe.grid(column=1, row=0, sticky=(N, W, E, S))
        # rightframe.rowconfigure(0, weight=1)
        # rightframe.columnconfigure(1, weight=1)
        m.add(rightframe, stretch="never", minsize=100)

        # m.add(top)
        #
        # m.add(bottom)

        tkinter.Frame.__init__(self)
        self.grid(sticky=N + S + E + W)

        self.selectionCallback = None

    def onSelection(self, callback):
        self.selectionCallback = callback

    def onselect(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        self.selectionCallback(index)

    def addMessage(self, message):
        self.listbox.insert(END, message)


if __name__ == "__main__":
    theme = Theme.Theme.loadFromFile("dark.theme")

    root = tkinter.Tk()
    root.title("tkNotebook Example")
    root['bg'] = theme["Window"]['background']

    msgLog = MessageLog(root, theme['MessageLog'], width=800, height=600)
    msgLog.pack()

    root.mainloop()

