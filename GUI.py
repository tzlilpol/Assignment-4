from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.filedialog import askopenfilename

import xlrd
import numpy as np
import pandas as pd
from DataPreparation import preProcessData
class Application:
    def __init__(self, master):
        self.master = master
        master.title("Assignment4")

        self.pathLabel = Label(master, text='File Path')
        self.filePath = StringVar()

        self.browseInput=Entry(master,width=50,borderwidth=1, textvariable=self.filePath)
        self.browseInput.grid(row=1,column=0)

        self.clustersInput=Entry(master,width=30,borderwidth=1)
        self.clustersInput.grid(row=3,column=0)

        self.runsInput=Entry(master,width=30,borderwidth=1)
        self.runsInput.grid(row=5,column=0)

        # Create a Label Widget
        self.pathChooseLbl=Label(master,text="Please enter dataset path:").grid(row=0,column=0)
        self.clustersLbl=Label(master,text="Number of clusters k:").grid(row=2,column=0)
        self.runsLbl=Label(master,text="Number of runs:").grid(row=4,column=0)
        #Create a buttons
        self.browseBtn=Button(master,text="Browse", command=lambda: self.openFile()).grid(row=1,column=1)
        self.preProcessBtn=Button(master,text="Pre-process", command=lambda:self.preProcessData()).grid(row=6,column=0)
        self.clusterBtn=Button(master,text="Cluster", command=lambda:self.buildModal()).grid(row=6,column=1)
        self.dataSet = None
        self.DataFrame = None

         # Functions
    def openFile(self):
        self.filePath.set(askopenfilename())

    def preProcessData(self):
        self.dataSet=pd.read_excel(self.filePath.get())
        print(self.dataSet)
        self.DataFrame = preProcessData(self.dataSet)
        messagebox.showinfo(title='K Means Clustering', message="Preprocessing completed successfully!")

    def buildModal(self):
        lbl = Label(self.master, text="Build Modal...").grid(row=7, column=1)

root = Tk()
my_gui=Application(root)
root.mainloop()