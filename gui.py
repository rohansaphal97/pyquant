from tkinter import *
from tkinter import filedialog
import trading
import utilities
import signals
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backend_bases import key_press_handler

# class window(Frame):
#     trading_data =  None
#     def __init__(self,master=None):
#         Frame.__init__(self,master)
#         self.createViews()
#     def createViews(self):
#         upload_csv_button = Button(text = "Open CSV", command = self.on_upload_csv_button_click())
#         upload_csv_button.pack()
#         stock_price_graph = FigureCanvasTkAgg()
#     def pass_file(self):
#         return filedialog.askopenfile(mode="r")
#     def on_upload_csv_button_click(self):
#         csv = self.pass_file()
#         self.trading_data = utilities.parse_csv(csv.name)
# def main():
#     root = Tk()
#     root.wm_title("QTS Trading Simulator")
#     root.geometry("250x150+300+300")
#     app = window()
#     root.mainloop()
# main()