from tkinter import *
import Backend.My_First_CB as ViASide

#BG_Gray = "#ABB2B9"
BG_Gray = "#54486d"
BG_Colour = "#252458"
Text_Colour = "#EAECEE"
Mssg_colour = "#2C3E50"
Bttn_Colour = "#808dd3"

Font = "Courier 13"
Font_Bold = "Helvetica 11 bold"


class ViA_GUI():
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    ##! Make Window
    def _setup_main_window(self):
        self.window.title("ViA Assistant")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=480, height=550, bg=BG_Colour)

        ##! Head Area
        head_label = Label(
            self.window,
            bg=BG_Colour,
            fg=Text_Colour,
            text=ViASide.session_prompt,
            font=Font_Bold,
            pady=10)  ####!!!! Use Bot Here, switch to instructions
        head_label.place(relwidth=1)

        ##*Tiny Divider
        line = Label(self.window, width=450, bg=BG_Gray)
        line.place(relwidth=1, rely=0.071, relheight=0.012)

        ##!Text Body
        self.textWidget = Text(self.window,
                               width=20,
                               height=2,
                               bg=BG_Colour,
                               fg=Text_Colour,
                               font=Font,
                               padx=2,
                               pady=2,
                               wrap=WORD)
        self.textWidget.place(relheight=0.744, relwidth=1, rely=0.08)
        self.textWidget.configure(cursor="arrow", state=DISABLED)

        ##!Scroll-Bar
        scrllbar = Scrollbar(self.textWidget)
        scrllbar.place(relheight=1, relx=0.999)
        scrllbar.configure(command=self.textWidget.yview)

        ##! Sender BG
        bottom_label = Label(self.window, bg=BG_Gray, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        ##! Mssg Entry
        self.mssgEntry = Entry(bottom_label,
                               bg=Mssg_colour,
                               fg=Text_Colour,
                               font=Font)
        self.mssgEntry.place(relwidth=0.74,
                             relheight=0.07,
                             rely=0.008,
                             relx=0.011)
        self.mssgEntry.focus()
        self.mssgEntry.bind("<Return>", self.onEnter)

        ##! A Send BUtton
        sendBttn = Button(bottom_label,
                          text="Ask ViA",
                          font=Font_Bold,
                          width=20,
                          bg=Bttn_Colour,
                          command=lambda: self.onEnter(None))
        sendBttn.place(relx=0.77, rely=0.008, relheight=0.07, relwidth=0.22)

        ##! Defining onEnter
    def onEnter(self, event):
        msg = self.mssgEntry.get()
        self._insertMssg(msg, "You")

    def _insertMssg(self, msg, sender):
        if not msg:
            return
        self.mssgEntry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.textWidget.configure(cursor="arrow", state=NORMAL)
        self.textWidget.insert(END, msg1)
        self.textWidget.configure(cursor="arrow", state=DISABLED)

        msg2 = f"{ViASide.BotName}: {ViASide.Ask(msg1)}\n\n"  ##! ViA Interaction text
        self.textWidget.configure(cursor="arrow", state=NORMAL)
        self.textWidget.insert(END, msg2)
        self.textWidget.configure(cursor="arrow", state=DISABLED)

        self.textWidget.see(END)


if __name__ == "__main__":
    app = ViA_GUI()
    app.run()
