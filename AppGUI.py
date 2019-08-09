#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from system_var import *


# root = tk.Tk()
# Frame = tk.Frame()
# Frame.grid()

class SystemVar():
    _renBySCRPT=""
    _dirPDF=""
    _Instdir=""
    _destFOLDER=""
    _TXTHostPCName=""
    _DestPCName=""
    _convert2PDF=""
    _UnidadEnRED=""
    _GETHostPCName=""
    _dirIMAGICK=""
    _RenameByGUI=""
    _LogFile=""
    _UseDate2Move=""

    t=VariablesSystemas()

    _renBySCRPT=t.VarUseRenByScrypt()
    _dirPDF=t.VarDirPDF()
    _Instdir=t.VarInstalationDir()
    _destFOLDER=t.VarDestinyFOLDER()
    _TXTHostPCName=t.VarHostPC()
    _DestPCName=t.VarDestinyPC()
    _convert2PDF=t.VarConvertToPDF()
    _UnidadEnRED=t.VarUndEnRED()
    _GETHostPCName=t.VarGetDomainName()
    _dirIMAGICK=t.VarImgMagickDir()
    _RenameByGUI=t.VarRenameByGUI()
    _LogFile=t.VarWriteLogFile()
    _UseDate2Move=t.VarUseDate2Move()

    def Get(self,valor):


        if valor== "VarUseRenByScrypt":
            return self._renBySCRPT
        elif valor== "VarDirPDF":
            return self._dirPDF
        elif valor== "VarInstalationDir":
            return self._Instdir
        elif valor== "VarDestinyFOLDER":
            return self._destFOLDER
        elif valor== "VarHostPC":
            return self._TXTHostPCName
        elif valor== "VarDestinyPC":
            return self._DestPCName
        elif valor== "VarConvertToPDF":
            return self._convert2PDF
        elif valor== "VarUndEnRED":
            return self._UnidadEnRED
        elif valor== "VarGetDomainName":
            return self._GETHostPCName
        elif valor== "VarImgMagickDir":
            return self._dirIMAGICK
        elif valor== "VarRenameByGUI":
            return self._RenameByGUI
        elif valor== "VarWriteLogFile":
            return self._LogFile
        elif valor== "VarUseDate2Move":
            return self._UseDate2Move


sysVar=SystemVar()



class fondoGUI():
    def __init__(self,var1):
        fondo=Toplevel()    
        fondo.title("VArchivo Detectado, Correccion de nombre")
        fondo.config(bg="gray")
        fondo.attributes('-alpha',0.6)
        fondo.attributes('-fullscreen',True)

        # os.chdir("..")
        # sysVar=VariablesSystemas()
        _Instdir=sysVar.Get("VarInstalationDir")
        _Ldir="{}{}".format(_Instdir,"/imagenes/")
        os.chdir(_Ldir)
        _archivoIMGname="calabaza.ico"
        #_archivoIMG="{}{}{}".format(_Instdir,"/imagenes/",_archivoIMGname)

        fondo.iconbitmap(_archivoIMGname)

class function_menuBar():
    def mabout(self):
        tk.messagebox.showinfo(title="About",message="""Hecho por: Yoka Alejandra Alvarez\nVersion: 0.0.1\n\n\ncorreo: Yoka.alvarezr@outlook.com""")
        return

class AppGUI2(tk.Tk):
    def __init__(self,_filename,_fileNamePreview,PreviewIMG):
        super().__init__()
        self.title("Archivo Detectado, Correccion de nombre")
        self.resizable(1,1)
        #self.geometry("650x350+100+200")  #  FOMRA QUE ME GUSTA ...PARA DAR TAMANO Y POSICION  OJO  ES AL MAIN FORM NO AL Frame
        self.attributes("-topmost",True)


        #print("entre en el root")

        #os.chdir("..")
        #sysVar=VariablesSystemas()
        _Instdir=sysVar.Get("VarInstalationDir")
        _Ldir="{}{}".format(_Instdir,"/imagenes/")
        os.chdir(_Ldir)
        _archivoIMGname="calabaza.ico"
        self.iconbitmap(_archivoIMGname)

        Frame = tk.Frame(self)
        Frame.grid()


        ###############################################
        #       construccion de las rejillas
        ###############################################
        Frame1 = tk.LabelFrame(Frame, text="Frame1", width=600, height=50, bd=5)
        Frame2 = tk.LabelFrame(Frame, text="Frame2", width=600, height=300, bd=5)
        Frame3 = tk.LabelFrame(Frame, text="Frame3", width=300, height=300, bd=5)
        Frame4 = tk.LabelFrame(Frame, text="Frame4", width=200, height=50, bd=5)
        Frame1.grid(row=0, column=0, columnspan=2, padx=8)
        Frame2.grid(row=1, column=0, padx=8)
        Frame3.grid(row=1, column=1, sticky='nw')
        Frame4.grid(row=2, column=1 )

        ###############################################
        #       construccion de las rejillas
        ###############################################
        self.PDFuserName = tk.StringVar()
        self.PDFuserLast = tk.StringVar()
        self.PDFuserNum = tk.StringVar()
        self._PDFfileType = tk.StringVar()

        tk.Label(Frame2, text="Enter customer's Name: ").grid(row=0, column=0, pady=10, sticky=tk.W)
        tk.Entry(Frame2, textvariable=self.PDFuserName).grid(row=0, column=1, padx=10, sticky=tk.E)

        tk.Label(Frame2, text="Enter customer's Last Name: ").grid(row=1, column=0, pady=10, sticky=tk.W)
        tk. Entry(Frame2, textvariable=self.PDFuserLast).grid(row=1, column=1, padx=10, sticky=tk.E)

        tk.Label(Frame2, text="Enter customer's Last 4 SSN: ").grid(row=2, column=0, pady=10, sticky=tk.W)        
        tk.Entry(Frame2, textvariable = self.PDFuserNum).grid(row=2, column=1, padx=10, sticky=tk.E)

        tk.Label(Frame2, text="Enter Document Type: ").grid(row=3, column=0, pady=10, sticky=tk.W)       
        tk.Entry(Frame2, textvariable = self._PDFfileType).grid(row=3, column=1, padx=10, sticky=tk.E)


        #_dirPDF=sysVar.Get("VarDirPDF")
        ###################################################################################
        #####     Comienza el Ingerto de cargar imagen redimencionada
        ###################################################################################
        # _dirPDF=sysVar.Get("VarDirPDF")
        # os.chdir(_dirPDF)
        # pic = tk.filedialog.askopenfilename()
        # print (pic)
        # img = Image.open(pic)

        # o_size = img.size   #Tamaño original de la imagen
        # f_size = (256, 256) #Tamaño del canvas donde se mostrará la imagen


        # factor = min(float(f_size[1])/o_size[1], float(f_size[0])/o_size[0])
        # width = int(o_size[0] * factor)
        # height = int(o_size[1] * factor)

        # rImg= img.resize((width, height), Image.ANTIALIAS)
        # rImg = ImageTk.PhotoImage(rImg)

        # canvas = tk.Canvas(Frame3, width=f_size[0], height= f_size[1])
        # canvas.create_image(f_size[0]/2, f_size[1]/2, anchor=tk.CENTER, image=rImg, tags="img")
        # canvas.pack(fill=None, expand=False)
        ###################################################################################
        #####     Finaliza el Ingerto 
        ###################################################################################
       
        tk.Button(Frame4, text="ACCEPT", command=self.on_accept).grid(row=0, column=0,sticky=tk.E + tk.W)

        # ##  CONSTRUCCION DEL OBJETOs-MENU QUE SERAN USDADOS PARA EJECUTAR LAS LLAMADAS DEL MENU ###
        
        objetosMenu=function_menuBar()

        ###     construccion del menu   ####
        menuBar=tk.Menu(self)

        #construccion del menu help
        helpmenu=tk.Menu(menuBar, tearoff=0)
        helpmenu.add_command(label="About",command=objetosMenu.mabout)
        helpmenu.add_command(label="Help")

        menuBar.add_cascade(label="About",menu=helpmenu)

        ### ensamblado del menu en el main form
        self.config(menu=menuBar)
        #self.mainloop()
        fondo=fondoGUI(self)
        self.mainloop()
    def on_accept(self):  
        # Puedes aprobechar esto para validar los datos antes de cerrar
        self.destroy()

    def get_data(self,_fileNamePreview,_PreviewIMG):
        # ACA SE HACE LA LLAMADA AL FONDO HABILITAR DE ALGUN MODO
        
        PDFuserName = self.PDFuserName.get()
        PDFuserLast = self.PDFuserLast.get()
        PDFuserNum = self.PDFuserNum.get()
        _PDFfileType = self._PDFfileType.get()
        return [PDFuserName, PDFuserLast, PDFuserNum, _PDFfileType]    
    

if __name__ == "__main__":
    
    _Instdir=sysVar.Get("VarInstalationDir")
    _Ldir="{}{}".format(_Instdir,"/imagenes/")
    _filename=os.path.join(_Ldir,"noimage.jpg")
    _fileNamePreview=""
    PreviewIMG=True
    formulario = AppGUI2(_filename,_fileNamePreview,PreviewIMG)
    print(formulario.get_data(True,None))