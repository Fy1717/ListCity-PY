from tkinter import *
class Sehir:
    def __init__(self):
        window=Tk()
        window.title("Turkiye-Sehirler")
        Label(window,text="Sehir Adi",width=10).grid(row=0,column=3,sticky=W)
        Label(window,text="Kisaltma",width=10).grid(row=3,column=3, sticky=W)
        Label(window,text="Nesi Meshur",width=10).grid(row=5,column=3,sticky=W)
        Label(window,text="Bolgesi",width=10).grid(row=7,column=3,sticky=W)
        Label(window,text="Plaka Kodu",width=10).grid(row=9,column=3,sticky=W)

        yscroll=Scrollbar(window,orient=VERTICAL)
        yscroll.grid(row=0,column=2,rowspan=12,pady=5,stick=NS)

        dosya=open("sehirler.txt",'r')
        symbolSet={line.split(',')[1] for line in dosya}
        dosya.close()

        symbolList=list(symbolSet)
        symbolList.sort()

        self.conOflstSymbols=StringVar()
        self._lstSymbols=Listbox(window,width=5, listvariable=self.conOflstSymbols, yscrollcommand=yscroll.set)
        self._lstSymbols.grid(row=1, column=1, rowspan=10, pady=5, sticky=E)
        self._lstSymbols.bind("<<ListboxSelect>>",self.facts)
        self.conOflstSymbols.set(tuple(symbolList))

        self.conOfentSehir=StringVar()
        self.entSehir=Entry(window,state="readonly",width=30,textvariable=self.conOfentSehir)
        self.entSehir.grid(row=2, column=3, columnspan=2, padx=5, sticky=W)

        self.conOfentNesimeshur=StringVar()
        self.entNesimeshur=Entry(window,state="readonly", width=30, textvariable=self.conOfentNesimeshur)
        self.entNesimeshur.grid(row=4, column=3, columnspan=2, padx=5, sticky=W)

        self.conOfentPlaka=StringVar()
        self.entPlaka=Entry(window,state="readonly",width=30,textvariable=self.conOfentPlaka)
        self.entPlaka.grid(row=6,column=3,columnspan=2,padx=5,sticky=W)

        self.conOfentBolge=StringVar()
        self.entBolge=Entry(window,state="readonly",width=30,textvariable=self.conOfentBolge)
        self.entBolge.grid(row=8,column=3,columnspan=2,padx=5,sticky=W)

        self.conOfentKisaltma=StringVar()
        self.entKisaltma=Entry(window,state="readonly",width=30,textvariable=self.conOfentKisaltma)
        self.entKisaltma.grid(row=10,column=3,columnspan=2,padx=5,sticky=W)

        yscroll["command"]=self._lstSymbols.yview
        window.mainloop()

    def at(self,e):
         print("at")

    def facts(self,e):
        symbol=self._lstSymbols.get(self._lstSymbols.curselection())
        dosya=open("sehirler.txt", 'r')
        while True:
            line= dosya.readline()
            lineList=line.split(',')
            if lineList[1]==symbol:
                break

        dosya.close()

        self.conOfentSehir.set(lineList[0])
        self.conOfentKisaltma.set(lineList[1])
        self.conOfentPlaka.set(lineList[2])
        self.conOfentBolge.set(lineList[3])
        self.conOfentNesimeshur.set(lineList[4])
Sehir()
         
         
        
