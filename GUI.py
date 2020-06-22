from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Assignment4")
browseInput=Entry(root,width=50,borderwidth=1)
browseInput.grid(row=1,column=0)

clustersInput=Entry(root,width=30,borderwidth=1)
clustersInput.grid(row=3,column=0)

runsInput=Entry(root,width=30,borderwidth=1)
runsInput.grid(row=5,column=0)
# e.delete(0,"")
path=""
#Functions
def openFile():
    path=filedialog.askopenfilename()
    browseInput.insert(0,path)
def preProcessData():
    lbl=Label(root,text="Data ready...").grid(row=7,column=0)
def buildModal():
    lbl=Label(root,text="Build Modal...").grid(row=7,column=1)

# Create a Label Widget
pathChooseLbl=Label(root,text="Please enter dataset path:")
clustersLbl=Label(root,text="Number of clusters k:")
runsLbl=Label(root,text="Number of runs:")
#Create a buttons
browseBtn=Button(root,text="Browse",command=openFile)
preProcessBtn=Button(root,text="Pre-process",command=preProcessData)
clusterBtn=Button(root,text="Cluster",command=buildModal)
# Shoving it onto screen
pathChooseLbl.grid(row=0,column=0)
clustersLbl.grid(row=2,column=0)
runsLbl.grid(row=4,column=0)
browseBtn.grid(row=1,column=1)
preProcessBtn.grid(row=6,column=0)
clusterBtn.grid(row=6,column=1)
root.mainloop()