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
        master.title("K Means Clustering")

        self.pathLabel = Label(master, text='File Path')
        self.filePath = StringVar()
        self.nClusters = StringVar()
        self.nInit = StringVar()

        self.browseInput=Entry(master,width=50,borderwidth=1, textvariable=self.filePath)
        self.browseInput.grid(row=1,column=0)

        self.clustersInput=Entry(master,width=30,borderwidth=1, textvariable=self.nClusters, state=DISABLED)
        self.clustersInput.grid(row=3,column=0)
        self.reg1 = self.master.register(self.clustersInputValidation)
        self.clustersInput.config(validate="key", validatecommand=(self.reg1, '%P'))

        self.runsInput=Entry(master,width=30,borderwidth=1, textvariable=self.nInit, state=DISABLED)
        self.runsInput.grid(row=5,column=0)
        self.reg2 = self.master.register(self.runsInputValidation)
        self.runsInput.config(validate="key", validatecommand=(self.reg2, '%P'))

        # Create a Label Widget
        self.pathChooseLbl=Label(master,text="Please enter dataset path:").grid(row=0,column=0)
        self.clustersLbl=Label(master,text="Number of clusters k:").grid(row=2,column=0)
        self.runsLbl=Label(master,text="Number of runs:").grid(row=4,column=0)
        #Create a buttons
        self.browseBtn=Button(master,text="Browse", command=lambda: self.openFile()).grid(row=1,column=1)
        self.preProcessBtn=Button(master,text="Pre-process", command=lambda:self.preProcessData()).grid(row=6,column=0)
        self.clusterBtn=Button(master,text="Cluster", command=lambda:self.buildModal(), state=DISABLED)
        self.clusterBtn.grid(row=6,column=1)
        self.dataSet = None
        self.DataFrame = None

        self.clusterError1 = Label()
        self.clusterError2 = Label()
        self.btnCheck1 = False
        self.btnCheck2 = False

    def clustersInputValidation(self,input):
        if not input:
            self.clusterError1.destroy()
            self.clusterError1 = Label(self.master, text="Cannot be empty", fg='red')
            self.clusterError1.grid(row=3, column=1)
            self.btnCheck1 = False
            self.clusterBtn.config(state=DISABLED)
            return True
        elif(not input.isdigit()):
            self.clusterError1.destroy()
            self.clusterError1 = Label(self.master, text="Text must consist of digits only", fg='red')
            self.clusterError1.grid(row=3, column=1)
            self.btnCheck1 = False
            self.clusterBtn.config(state=DISABLED)
            return True
        elif(int(input)<2):
            self.clusterError1.destroy()
            self.clusterError1 = Label(self.master, text="Value cannot be smaller then 2", fg='red')
            self.clusterError1.grid(row=3, column=1)
            self.btnCheck1 = False
            self.clusterBtn.config(state=DISABLED)
            return True
        else:
            self.clusterError1.destroy()
            self.btnCheck1 = True
            if(self.btnCheck2 == True):
                self.clusterBtn.config(state=NORMAL)
            return True

    def runsInputValidation(self,input):
        if not input:
            self.clusterError2.destroy()
            self.clusterError2 = Label(self.master, text="Cannot be empty", fg='red')
            self.clusterError2.grid(row=5, column=1)
            self.btnCheck2 = False
            self.clusterBtn.config(state=DISABLED)
            return True
        elif (not input.isdigit()):
            self.clusterError2.destroy()
            self.clusterError2 = Label(self.master, text="Text must consist of digits only", fg='red')
            self.clusterError2.grid(row=5, column=1)
            self.btnCheck2 = False
            self.clusterBtn.config(state=DISABLED)
            return True
        elif (int(input) <= 0):
            self.clusterError2.destroy()
            self.clusterError2 = Label(self.master, text="Value cannot be smaller then 0", fg='red')
            self.clusterError2.grid(row=5, column=1)
            self.btnCheck2 = False
            self.clusterBtn.config(state=DISABLED)
            return True
        else:
            self.clusterError2.destroy()
            self.btnCheck2 = True
            if (self.btnCheck1 == True):
                self.clusterBtn.config(state=NORMAL)
            return True

    # Functions
    def openFile(self):
        self.filePath.set(askopenfilename())

    def preProcessData(self):
        try:
            self.dataSet=pd.read_excel(self.filePath.get())
            print(self.dataSet)
            self.DataFrame = preProcessData(self.dataSet)
            print(self.DataFrame)
            messagebox.showinfo(title='K Means Clustering', message="Preprocessing completed successfully!")
            self.clustersInput.config(state=NORMAL)
            self.runsInput.config(state=NORMAL)
        except FileNotFoundError:
            messagebox.showerror(title='File Not Found', message='Please choose an existing datafile')

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
        messagebox.showinfo(title='K Means Clustering', message="K Means Clustering completed successfully!")

    def exit(self):
        self.master.destroy()

root = Tk()
my_gui=Application(root)
root.mainloop()