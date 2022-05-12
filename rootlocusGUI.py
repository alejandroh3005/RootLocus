from rootlocusplot import RLPlotting
import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

if __name__ == "__main__":
    # create and setup window
    root = tk.Tk()
    width, height = 600, 400
    canvas1 = tk.Canvas(root, width=width, height=height)
    canvas1.pack()
    # prompt user for numerator coefficients
    numLabel = tk.Label(root, text="numerator coefficients with space as separator")
    canvas1.create_window(width/2, 20, window=numLabel)
    numEntry = tk.Entry(root)
    canvas1.create_window(width/2, 40, window=numEntry)
    # prompt user for denominator coefficients
    denLabel = tk.Label(root, text="denominator coefficients with space as separator")
    canvas1.create_window(width/2, 60, window=denLabel)
    denEntry = tk.Entry(root)
    canvas1.create_window(width/2, 80, window=denEntry)

    # function to embed plot in window
    def plotRL():
        numerator = [int(i) for i in numEntry.get().split()]
        denominator = [int(i) for i in denEntry.get().split()]
        RL = RLPlotting(numerator, denominator)

        # display RL information
        RLInfo = tk.Label(root, text=RL)
        canvas1.create_window(width/2, 250, window=RLInfo)

        # display plot outside window
        ax, fig = RL.plot()
        plt.show()
        # TODO: complete plot embedding
        """
        # embed generated plot in GUI window
        ax, fig = RL.plot()
        chart_type = FigureCanvasTkAgg(fig, root)
        chart_type.get_tk_widget().pack()
        plt.plot(legend=True, ax=ax)
        ax.set_title('Root Locus Plot')
        """

    # button to generate and display plot
    plotIt = tk.Button(text="plot it!", command=plotRL)
    canvas1.create_window(width/2, 110, window=plotIt)
    root.mainloop()