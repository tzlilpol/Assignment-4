from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.filedialog import askopenfilename

import xlrd
import numpy as np
import pandas as pd
from PIL import ImageTk
from PIL import Image

from DataPreparation import preProcessData
from kmeans import *


class Application:
    def __init__(self, master):
        self.master = master
        master.title("Assignment4")

        self.pathLabel = Label(master, text='File Path')
        self.filePath = StringVar()
        self.nClusters = StringVar()
        self.nInit = StringVar()

        self.browseInput=Entry(master,width=50,borderwidth=1, textvariable=self.filePath)
        self.browseInput.grid(row=1,column=0)

        self.clustersInput=Entry(master,width=30,borderwidth=1, textvariable=self.nClusters)
        self.clustersInput.grid(row=3,column=0)

        self.runsInput=Entry(master,width=30,borderwidth=1, textvariable=self.nInit)
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
        print(self.DataFrame)
        messagebox.showinfo(title='K Means Clustering', message="Preprocessing completed successfully!")

    def buildModal(self):
        self.lbl = Label(self.master, text="Build Modal...")
        self.lbl.grid(row=7, column=1)
        kmean= kMeans()
        kmean.k_means_modeling(self.DataFrame, self.nClusters.get(), self.nInit.get())
        print(self.DataFrame)
        kmean.scatter(self.DataFrame, self.filePath.get())
        kmean.horoplethMap(self.DataFrame, self.filePath.get())
        self.lbl.destroy()
        scatterImg = ImageTk.PhotoImage(Image.open(os.path.dirname(self.filePath.get())+'/scatter.png'))
        self.scatter=Label(self.master, image = scatterImg)
        self.scatter.grid(row=8,column=1)
        self.scatter.image = scatterImg
        choroplethImg = ImageTk.PhotoImage(Image.open(os.path.dirname(self.filePath.get()) + '/choropleth.png'))
        self.choropleth = Label(self.master, image=choroplethImg)
        self.choropleth.grid(row=8, column=0)
        self.choropleth.image = choroplethImg

root = Tk()
my_gui=Application(root)
root.mainloop()