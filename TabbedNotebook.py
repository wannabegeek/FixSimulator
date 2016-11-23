import tkinter
from tkinter.constants import *

class Notebook(tkinter.Frame):
    """Notebook Widget"""

    def __init__(self, parent, theme, activerelief=RIDGE, inactiverelief=RAISED, xpad=6, ypad=3, **kw):
        """Construct a Notebook Widget

        Notebook(self, parent, activerelief = RAISED, inactiverelief = RIDGE, xpad = 4, ypad = 6, activefg = 'black', inactivefg = 'black', **kw)

        Valid resource names: background, bd, bg, borderwidth, class,
        colormap, container, cursor, height, highlightbackground,
        highlightcolor, highlightthickness, relief, takefocus, visual, width, activerelief,
        inactiverelief, xpad, ypad.

        xpad and ypad are values to be used as ipady and ipadx
        with the Label widgets that make up the tabs. activefg and inactivefg define what
        color the text on the tabs when they are selected, and when they are not

        """
        # Make various argument available to the rest of the class
        self.theme = theme
        self.deletedTabs = []
        self.xpad = xpad
        self.ypad = ypad
        self.activerelief = activerelief
        self.inactiverelief = inactiverelief
        self.kwargs = kw
        self.tabVars = {}  # This dictionary holds the label and frame instances of each tab
        self.tabs = 0  # Keep track of the number of tabs
        self.noteBookFrame = tkinter.Frame(parent)  # Create a frame to hold everything together
        self.noteBookFrame["bg"] = self.theme['border']
        self.BFrame = tkinter.Frame(self.noteBookFrame)  # Create a frame to put the "tabs" in
        self.noteBook = tkinter.Frame(self.noteBookFrame, bd=2, **kw)  # Create the frame that will parent the frames for each tab
        self.noteBook["bg"] = self.theme['border']
        self.noteBook.grid_propagate(0)  # self.noteBook has a bad habit of resizing itself, this line prevents that
        tkinter.Frame.__init__(self)
        self.noteBookFrame.grid(sticky=N+E+S+W)
        self.BFrame.grid(row=0, sticky=W)
        self.noteBook.grid(row=1, column=0, columnspan=27, sticky=N+E+S+W)

        self.noteBook.grid_rowconfigure(0, weight=1)
        self.noteBook.grid_columnconfigure(0, weight=1)

        self.noteBookFrame.grid_rowconfigure(1, weight=1)
        self.noteBookFrame.grid_columnconfigure(0, weight=1)

    def change_tab(self, IDNum):
        """Internal Function"""

        for i in (a for a in range(0, len(self.tabVars.keys()))):
            if not i in self.deletedTabs:  # Make sure tab hasen't been deleted
                if i != IDNum:  # Check to see if the tab is the one that is currently selected
                    self.tabVars[i][1].grid_remove()  # Remove the Frame corresponding to each tab that is not selected
                    self.tabVars[i][0]['relief'] = self.theme['inactiveTabRelief']  #  # Change the relief of all tabs that are not selected to "Groove"
                    self.tabVars[i][0]['fg'] = self.theme['inactiveTabText']  # Set the fg of the tab, showing it is selected, default is black
                    self.tabVars[i][0]['bg'] = self.theme['inactiveTab']  # Set the fg of the tab, showing it is selected, default is black
                else:  # When on the tab that is currently selected...
                    self.tabVars[i][1].grid(sticky=N+E+S+W)  # Re-grid the frame that corresponds to the tab
                    self.tabVars[IDNum][0]['relief'] = self.theme['inactiveTabRelief']  # Change the relief to "Raised" to show the tab is selected
                    self.tabVars[i][0]['fg'] = self.theme['activeTabText']  # Set the fg of the tab, showing it is not selected, default is black
                    self.tabVars[i][0]['bg'] = self.theme['activeTab']  # Set the fg of the tab, showing it is not selected, default is black

    def add_tab(self, width=2, **kw):
        """Creates a new tab, and returns it's corresponding frame

        """

        temp = self.tabs  # Temp is used so that the value of self.tabs will not throw off the argument sent by the label's event binding
        self.tabVars[self.tabs] = [tkinter.Label(self.BFrame, relief=RIDGE, **kw)]  # Create the tab
        self.tabVars[self.tabs][0].bind("<Button-1>", lambda Event: self.change_tab(temp))  # Makes the tab "clickable"
        self.tabVars[self.tabs][0].pack(side=LEFT, ipady=self.ypad, ipadx=self.xpad)  # Packs the tab as far to the left as possible
        self.tabVars[self.tabs].append(tkinter.Frame(self.noteBook, **self.kwargs))  # Create Frame, and append it to the dictionary of tabs
        self.tabVars[self.tabs][1].grid(row=0, column=0)  # Grid the frame ontop of any other already existing frames
        self.change_tab(0)  # Set focus to the first tab
        self.tabs += 1  # Update the tab count
        return self.tabVars[temp][1]  # Return a frame to be used as a parent to other widgets

    def destroy_tab(self, tab):
        """Delete a tab from the notebook, as well as it's corresponding frame

        """

        self.iteratedTabs = 0  # Keep track of the number of loops made
        for b in self.tabVars.values():  # Iterate through the dictionary of tabs
            if b[1] == tab:  # Find the NumID of the given tab
                b[0].destroy()  # Destroy the tab's frame, along with all child widgets
                self.tabs -= 1  # Subtract one from the tab count
                self.deletedTabs.append(self.iteratedTabs)  # Apend the NumID of the given tab to the list of deleted tabs
                break  # Job is done, exit the loop
            self.iteratedTabs += 1  # Add one to the loop count

    def focus_on(self, tab):
        """Locate the IDNum of the given tab and use
        change_tab to give it focus

        """

        self.iteratedTabs = 0  # Keep track of the number of loops made
        for b in self.tabVars.values():  # Iterate through the dictionary of tabs
            if b[1] == tab:  # Find the NumID of the given tab
                self.change_tab(self.iteratedTabs)  # send the tab's NumID to change_tab to set focus, mimicking that of each tab's event bindings
                break  # Job is done, exit the loop
            self.iteratedTabs += 1  # Add one to the loop count