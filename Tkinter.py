import tkinter as tk
import Soup

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createwidgets()

    def createwidgets(self):
        z = Soup.Soup.bitcoin(self)
        print(z)
        self.out_price = tk.Label(self,text = "Price of bitcoin in PLN is " +  z)
        self.out_price.config(font=("Courier", 24))
        self.out_price.pack(side = "top")



    def upd(self):
        pass

    def out_price(self):
        pass



root = tk.Tk()
app = Application(master=root)
app.mainloop()
