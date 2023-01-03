import  tkinter as tk 
import requests
import json 

def  loadData():
    url="https://api.covid19api.com/summary"
    res=requests.get(url)
    return res.json()

data=loadData()

def parse():
    country_name=CountryBox.get().title()
    for country in data['Countries']:
        if country_name==country["Country"].title():
            resLabel.config(text=f"{country}")
            return
            
    resLabel.config(text="Invalid Country name")


root=tk.Tk()
CountryBox=tk.Entry(root)
btn=tk.Button(root,text="Submit",command=parse)
resLabel=tk.Label(root,text='')
CountryBox.grid(row=0,column=0)
btn.grid(row=0,column=1)
resLabel.grid(row=1)


root.mainloop()
