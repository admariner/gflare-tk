from tkinter import ttk, Toplevel, TOP


class ProgressWindow(Toplevel):

    def __init__(self, title=None, msg=None):
        Toplevel.__init__(self)

        self.topframe = ttk.Frame(self)
        self.topframe.pack(anchor='center', padx=20, pady=20, fill="x")

        if title:
            self.title(title)
        if msg:
            self.lbl = ttk.Label(self.topframe, text=msg)
            self.lbl.pack(padx=20, pady=20, side=TOP, expand=True)

        self.pb = ttk.Progressbar(
            self.topframe, orient='horizontal', mode='indeterminate')
        self.pb.pack(fill="x", pady=(0, 20), padx=20, side=TOP, expand=True)
        self.pb.start(50)

        # The window needs to be placed after its elements have been assigned
        # get window width and height

        height = self.master.winfo_height()
        width = self.master.winfo_width()

        pop_up_height = self.winfo_height()
        pop_up_width = self.winfo_width()

        x = self.master.winfo_rootx()
        y = self.master.winfo_rooty()

        x_offset = width // 2 - 2 * pop_up_width
        y_offset = height // 2 - pop_up_height

        # and where it is placed
        self.geometry('+%d+%d' % (x + x_offset, y // 2 + y_offset))
        self.lift()
