import pandas as pd

class Person:
    def __init__(self,name):
        self.name = name 

    def getName(self):
        datab = {'Name':['John','Sarah','Tony'],
        'Age':[28,26,32]}

        df= pd.DataFrame(datab,index=['rank1','rank2','rank3'])
        return df.to_excel("MyExcal.xlsx")
