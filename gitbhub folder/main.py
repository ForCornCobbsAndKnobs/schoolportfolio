from tkinter import *
import math


class ButtonDemo(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Roof Estimate")
        self.grid()



        Label(self, text='Enter Length (ft)').grid(row=0, column=1, padx=5, pady=10)

        self._box1var = IntVar()
        self._name1 = Entry(self, width=12, textvariable=self._box1var)
        self._name1.grid(row=0, column=0, padx=5, pady=10)

        Label(self, text='Enter Width (ft)').grid(row=1, column=1, padx=5, pady=10)

        self._box2var = IntVar()
        self._name2 = Entry(self, width=12, textvariable=self._box2var)
        self._name2.grid(row=1, column=0, padx=5, pady=10)

        Label(self, text='Enter rise(1-12)').grid(row=2, column=1, padx=5, pady=10)

        self._box3var = IntVar()
        self._name3 = Entry(self, width=12, textvariable=self._box3var)
        self._name3.grid(row=2, column=0, padx=5, pady=10)

        self._cb1Var = BooleanVar()
        Checkbutton(self, text='add 2 feet for eaves', variable=self._cb1Var).grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self._rb1 = IntVar()
        Radiobutton(self, text="20 year shingle", variable=self._rb1, value=20).grid(row=4, column=0, columnspan=1, padx=5, pady=10)

        Radiobutton(self, text="30 year shingle", variable=self._rb1, value=30).grid(row=4, column=1, columnspan=2, padx=5, pady=10)

        self._button1 = Button(self, text="Calculate Total", command=self._calcTotal)
        self._button1.grid(row=5, column=0, padx=10, pady=20)

        self._button2 = Button(self, text="Clear Form", command=self._clearInputs)
        self._button2.grid(row=5, column=1, padx=10, pady=20)

        self._box4var = IntVar()
        self._name4 = Entry(self, width=12, textvariable=self._box4var)
        self._name4.grid(row=6, column=0, padx=10, pady=20)

        Label(self, text='Estimated Total (in dollars)').grid(row=6, column=1, padx=10, pady=20)

    def _calcTotal(self):
        length = self._box1var.get()
        width = self._box2var.get()
        if self._cb1Var.get():
            width = width + 2
        pitch = math.sqrt(((self._box3var.get()) ** 2) + 144)
        pitch = round(pitch, 3)
        pitch = pitch / 12
        area = length * width * pitch
        price = self._rb1.get()
        if price == 20:
            price = round((area * 1.1 * 3.25), 2)
        elif price == 30:
            price = round((area * 1.1 * 3.75), 2)

        self._box4var.set(price)

    def _clearInputs(self):
        self._box1var.set(0)
        self._box2var.set(0)
        self._box3var.set(0)
        self._cb1Var.set(False)
        self._rb1.set(None)
        self._box4var.set(0)
def main():
    ButtonDemo().mainloop()


main()
