from rootlocusplot import RLPlotting
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    canvas1 = tk.Canvas(root, width=400, height=300)
    canvas1.pack()
    numLabel = tk.Label(root, text="numerator coefficients with space as seperator")
    canvas1.create_window(300, 20, window=numLabel)
    numEntry = tk.Entry(root)
    canvas1.create_window(300, 40, window=numEntry)
    denLabel = tk.Label(root, text="denominator coefficients with space as seperator")
    canvas1.create_window(300, 60, window=denLabel)
    denEntry = tk.Entry(root)
    canvas1.create_window(300, 80, window=denEntry)
    def plotRL():
        numerator = [int(i) for i in numEntry.get().split()]
        denominator = [int(i) for i in denEntry.get().split()]
        RL = RLPlotting(numerator, denominator)
        RLInfo = tk.Label(root, text=RL)
        canvas1.create_window(300, 250, window=RLInfo)
        RL.plot()
    plotIt = tk.Button(text="plot it!", command=plotRL)
    canvas1.create_window(300, 100, window=plotIt)
    root.mainloop()
