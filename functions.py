########################
#   IMPORTANDO FUNCIONES PROPIAS
#########################
#from objetos_dir import *
from GEimport import *
from system_var import *
#from build import SystemVar
#   FUNCIONES PROPIAS PARA PRUEBAS
from aoogyi2 import *
from pdf2png import *
from alphaOFF import *
#########################
#   IMPORTANDO LIBRERIAS ESTANDAR
#########################
# import tkinter as tk
# from tkinter import *
# from tkinter import messagebox
# from pdf2jpg import pdf2jpg
import sys
#import subprocess
#from preview_generator.manager import PreviewManager
#from AppGetName.modulos.menu_function import *
#########################
#   IMPORTANDO PARA PREVIEW
#########################
#import pypdfocr.pypdfocr_gs as pdfImg
from PIL import Image, ImageTk
#from wand.image import Image as WandImage
#    
# import ttk
# import glob
#from AppGUI import *




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



class ManejarObjFile():
    _LObjBE=[]
    _LObjAF=[]

    def ObjFile(self, nombre_archivo, ultima_modificacion, ultima_acceso, tamano_Kb, ubucacion_archivo, _TYPE):

        self.dicc={"_nomFILE":nombre_archivo,"_lastMOD":ultima_modificacion,"_lastACS":ultima_acceso,"_weigthKB":tamano_Kb,"_dirPDF":ubucacion_archivo}
        print("\n\nse tomo nuevo status con llamada desde un \"\"", _TYPE,"\"\"", self.dicc)
        print (self.dicc)
        if _TYPE=="BEFORE":
            self.addListaObjFileBEFORE(self.dicc)
        else:
            self.addListaObjFileAFTER(self.dicc)

    def GETListaObjBE(self):
        return self._LObjBE

    def GETListaObjAF(self):
        return self._LObjAF[:]

    def GET_ListaAfter(self):
        AA=[]
        for i in self._LObjAF:
            AA.append(i["_nomFILE"])
        return AA[:]
        AA=None

    def GET_ListaBefore(self):
        AA=[]
        print("en lista before")
        print("el diccionario before es: ",self._LObjBE , " y su id de memoria es:", id(self._LObjBE))
        for i in self._LObjBE:
            AA.append(i["_nomFILE"])
        print("la lista de nombres es: ",AA)
        return AA[:]
        

    def MODListaObjBE(self,valor):
        self._LObjBE=valor

    def CLEARListaObjAF(self):
        print(" print antes del clear: ",self._LObjAF )
        self._LObjAF.clear()
        print(" print despues en el clear: ",self._LObjAF )

    def CLEARListaObjBE(self):
        print(" \nprint antes del clear: ",self._LObjBE )
        self._LObjBE.clear()
        print(" \nprint despues en el clear: ",self._LObjBE )

    def addListaObjFileBEFORE(self,_OBJ):
        print ("\n\nENTRANDO en el addlist del BEFORE y la lista BEFORE es :",self._LObjBE[:])
        print ("\n\nENTRANDO en el addlist del before y la lista before es :",self._LObjBE[:])
        self.COMPROBAR(self._LObjBE[:],"Lista _LObjBE")
        
        print("\n\nel objeto a agregar en la lista es: ",_OBJ)
        
        self._LObjBE.append(_OBJ)
        
        self.COMPROBAR(self._LObjBE[:],"LUEGO DE APPEND _LObjBF")

        print ("\n\nSALIENDO DEL addlist del before y la lista before es :",self._LObjBE[:])

    def COMPROBAR(self, _object,_nombre):
        ### BORRAR DESDE ACA 1111   ESTO ES SOLO PAA COMPROVACION DE CODIGO
        AA=[]
        for i in _object:
            AA.append(i["_nomFILE"])
        print ("\nEl archivo << ",_nombre," >> tiene \" ",len(AA)," \" y son: \n",AA[:])
        AA=None
        ### BORRAR HASTA ACA 1111   ESTO ES SOLO PAA COMPROVACION DE CODIGO


    def addListaObjFileAFTER(self,_OBJ):
        self.COMPROBAR(self._LObjAF[:],"Lista _LObjAF")
                
        self._LObjAF.append(_OBJ)
        
        self.COMPROBAR(self._LObjAF[:],"LUEGO DE APPEND _LObjAF")
        
    def ShowObjectsListaBefore(self):
        total = 0
        linea = '-' * 40
        # Se acumulan tamaños y se muestra info de cada archivo
        for a in self._LObjBE:
            tamano=0
            print(linea)
            print('archivo      :', a["_nomFILE"])
            print('modificado   :', a["_lastMOD"])       
            print('ultimo acceso:', a["_lastACS"])
            tamano=round(int(a["_weigthKB"])/1024, 1)
            print('tamano (Kb)  :', tamano)
            print("Ubicacion del archivo: ",a["_dirPDF"],"\n")
            total= total+tamano

        print(linea)
        print(linea)
        print('Num. archivos:', len(self._LObjBE))
        print('Total (kb)   :', total)

    def GETStateFolder(self,_dirPDF,TYPE):
        #print(_dirPDF)
        _TYPE=TYPE
        print("\n\nEntre en el GETStatus desde un : \"\"", _TYPE,"\"\"")
        print("el valor de _dirPDF es : ",_dirPDF)
        contenido = os.listdir(_dirPDF)  # obtiene lista con archivos/dir 
        total = 0
        archivos = 0
        formato = '%d-%m-%y %H:%M:%S'  # establece formato de fecha-hora
        linea = '-' * 40

        for elemento in contenido:
            archivo = '{}{}{}'.format(_dirPDF,"/", elemento)
            #esto no desblquear...
            #print(archivo)
            #print(os.access(archivo, os.X_OK))
            #print(os.path.isfile(archivo))
            if os.access(archivo, os.X_OK) and os.path.isfile(archivo):
                archivos += 1
                estado = os.stat(archivo)  # obtiene estado del archivo
                tamano = estado.st_size  # obtiene de estado el tamaño 
                
                # Obtiene del estado fechas de último acceso/modificación
                # Como los valores de las fechas-horas vienen expresados
                # en segundos se convierten a tipo datetime. 
                
                ult_acceso = datetime.fromtimestamp(estado.st_atime)
                modificado = datetime.fromtimestamp(estado.st_mtime)
                
                # Se aplica el formato establecido de fecha y hora
                
                ult_acceso = ult_acceso.strftime(formato)
                modificado = modificado.strftime(formato)
                
        
                print(" se estan pasando los valores ",elemento," , ", modificado," , ", ult_acceso," , ", tamano," , ", _dirPDF," , ", _TYPE," GETStateFolder al constructor de objetos")
                self.ObjFile(elemento, modificado, ult_acceso, tamano, _dirPDF, _TYPE)


MngObj=ManejarObjFile()


class FunctionsClass():

    def __init__(self):
        print("\nEn Funcion << __init__ >> De <<< FunctionsClass >>> con PID# ",os.getpid())

        self._PDFdatos = []

    def OutPrint(self,*salida):
        print("\nEn Funcion << OutPrint >> con PID# ",os.getpid())
        _salida=" ".join(salida)
        _LogFile=sysVar.Get("VarWriteLogFile")
        _Instdir=sysVar.Get("VarInstalationDir")
        os.chdir(_Instdir)
        _time=str(datetime.now())
        if _LogFile==True:
            ###  escribir datos en el archivo
            from io import open 
            with open("Checkdir.Log","a") as _texto:
                ###  escritura de la lista en el archivo texton una variable por linea
                    _texto.write(_time+": "+_salida+"\n")
            _texto.close()
        else:
            _salida2="{}{}{}".format(_time,": ",salida)
            print(_salida2)

    def DirChangeDetect(self):
        print("\nEn Funcion << DirChangeDetect >> con PID# ",os.getpid())
        MngObj.CLEARListaObjAF()
        MngObj.GETStateFolder(sysVar.Get("VarDirPDF"),"AFTER")
        #############################################################
        #               comienza el ingerto
        #############################################################
        _change=False
        _LObjBE=MngObj.GETListaObjBE()
        _LObjAF=MngObj.GETListaObjAF()

        if _LObjAF == _LObjBE:
            print ("\n\nno hay cambios en la carpeta")
        else:
            print("\n*******  SE HA DETECTADO UN CAMBIO LA CARPETA... ACTUALIZANDO!!!    *********")
            MngObj.MODListaObjBE(_LObjAF)
            print("\n<<<<<  ACTUALIZADO  >>>>>\n")
            _change=True
        return _change
        #############################################################
        #               termina el ingerto
        #############################################################

    def Limpieza(self):
        print("\nEn Funcion << Limpieza >> con PID# ",os.getpid())
        os.chdir(sysVar.Get("VarDirPDF"))
        self.DirChangeDetect()
        _LObjBE=MngObj.GETListaObjBE()
        for i in _LObjBE:
            if int(i["_weigthKB"]) == 0:
                _archivo='{}{}{}'.format(sysVar.Get("VarDirPDF"),"/",i["_nomFILE"])
                print("el archivo a borrar es:\" ",_archivo , "\"")
                os.remove(_archivo)
                print("BORRANDO: ",_archivo)

        self.DirChangeDetect()

            
    def ConvertToPDF(self,_dirPDF,_dirIMAGICK):
        
        print("\nEn Funcion << ConvertToPDF >> con PID# ",os.getpid())
        os.chdir(_dirPDF)
        MngObj.CLEARListaObjBE()
        MngObj.GETStateFolder(sysVar.Get("VarDirPDF"),"BEFORE")
        ListName=MngObj.GET_ListaBefore()
        print("\nLa lista BEFORE en la funcion convertira pdf es: ",ListName)

        IMG=[".jpg",".JPG",".jpeg",".JPEG",".PNG",".png",".BMP","bmp"]
        for filename in ListName:
            file_name, file_extension = os.path.splitext(filename)
            if file_extension==IMG[0] or file_extension==IMG[2] or file_extension==IMG[3] or file_extension==IMG[4] or file_extension==IMG[5] or file_extension==IMG[6] or file_extension==IMG[7] :

                print("\nDirectorio de Conversion: ",os.getcwd())
                print("Nombre de archivo: ",file_name)
                print("Extencion: ",file_extension)

                im = Image.open(filename, 'r')
                _filePDFname="{}{}".format(file_name,".pdf")
                if im.mode == 'RGBA' or im.mode == 'SRGBA':
                    print("im.mode = ",im.mode )
                    print("la imagen contiene alpha channel")
                    print("convirtiendo la imagen a RGB")
                    #imgDestino="{}{}{}".format(file_name,"_sinALPHA",file_extension)
                    alphaOFF(3,filename,file_extension.replace(".",""),None,80,_dirPDF,None)

                    with open(_filePDFname,"wb") as f:
                        f.write(img2pdf.convert(filename))
                else:
                    print("im.mode = ",im.mode)
                    print("la imagen NO contiene alpha channel")
                    
                    with open(_filePDFname,"wb") as f:
                        f.write(img2pdf.convert(filename))

            elif file_extension==".PDF" or file_extension==".pdf":
                
                print("\nDirectorio de Conversion: ",os.getcwd())
                print("Nombre de archivo: ",file_name)
                print("Extencion: ",file_extension)


        self.Limpieza()

   
    #   Generate a thumbnail of an image file
    def Preview(self,file_name,file_extension,_filename):
        print("\nEn Funcion << Preview >> con PID# ",os.getpid())
        IMG=[".jpg",".JPG",".jpeg",".JPEG",".PNG",".png",".BMP",".bmp"]
        PDF=[".PDF",".pdf"]
        _dirPDF=sysVar.Get("VarDirPDF")
        _Instdir=sysVar.Get("VarInstalationDir")
        _thumbFOLDER="{}{}{}".format(_Instdir,"/imagenes","/thumb/")
        _file="{}{}".format(file_name,file_extension)
        _file_="{}{}{}{}{}".format("\"",_dirPDF,"/",_file,"\"")
        _filePNG="{}{}".format(file_name,".png")
        _filePNG2="{}{}{}".format(file_name,"2",".png")
        print("se entro en la funcion Preview con el archivo:",_file)
        os.chdir(_dirPDF)
        print("comparacion en FOR IMG")
        for i in IMG:
            print("Preview; Comparando= file_extension: >>> ",file_extension," <<< &  >>> ",i," <<<") 
            if file_extension == i:
                print("dentro de if del FOR IMG de funcion Preview , con archivo: ",_file_)
                _PreviewIMG=True
                x=""
        print("comparacion en FOR PDF")
        for i in PDF:
            print("Preview; Comparando= file_extension: >>> ",file_extension," <<< &  >>> ",i," <<<") 
            if(file_extension == i):
                _PreviewIMG=False
                obj=pdf2png()
                R=obj.convert2png(_file,_filePNG,_filePNG2,70)
                print("\nEl retorno de convert2png es: ",R)
            x=_filePNG2

        return [_PreviewIMG,x]

    def CambiarNombres(self,_dirPDF,_convert2PDF):

        print("\nEn Funcion << CambiarNombrePDF >> con PID# ",os.getpid())
        _convertToPDF=False     

        os.chdir(_dirPDF)
        ListName=MngObj.GETListaObjBE()

        #definicion de las variables que formaran el nombre para cada archivo
        _Instdir=sysVar.Get("VarInstalationDir")
        #define si dentro del cambio de nombre por script se hace por gui o por shell
        _RenameByGUI=sysVar.Get("VarRenameByGUI")

        for filename in ListName:
            #os.rename(filename, filename[5:])     #esta forma recorte el nombre
            print("\nla variable filename es: >>> ",filename)
            
            if _RenameByGUI==True:
                print("\nentre en el IF del Rename by GUI")

                #LLAMANDO A LA APPGUI PARA INGRESAR DATOS DE USUARIO
                #determinando la extencion del archivo
                _filename=filename["_nomFILE"]
                file_name, file_extension = os.path.splitext(_filename)
                _lista=self.Preview(file_name,file_extension,_filename)
                if _lista[0]==True:
                    _PreviewIMG=_lista[0]
                    _fileNamePreview=_lista[1]
                else:
                     _PreviewIMG=_lista[0]
                     _fileNamePreview=_lista[1]
                     
                print("la variable _filename llamando a AppGUI2: ",_filename)
                formulario = AppGUI2(_filename,_fileNamePreview,_PreviewIMG)

                _PDFdatos=formulario.get_data(_fileNamePreview,_PreviewIMG)
                print("\n<<<<  continuo la ejecuncion desde el punto despues de ir por los nombres >>>")

                print("\nEl nombre recibido de la AppGUI es: ",_PDFdatos)
                print("\nEse nombre en forma de lista tiene: ",len(_PDFdatos), " campos")
                _PDFuserName=_PDFdatos[0]
                _PDFuserLast=_PDFdatos[1]
                _PDFuserNum=_PDFdatos[2]
                _PDFfileType=_PDFdatos[3]
                print("\nlos valores que devuelve el GetName antes de formato son:", _PDFuserName," ", _PDFuserLast," ", _PDFuserNum," ", _PDFfileType)
                #_PDFname=self._PDFname.replace(" ","_")
                _PDFuserName=_PDFuserName.replace(" ","_")
                _PDFuserLast=_PDFuserLast.replace(" ","_")
                _PDFuserNum=_PDFuserNum.replace(" ","_")
                _PDFfileType=_PDFfileType.replace(" ","_")
                # print("\nlos valores que devuelve el GetName despues de formato son:", _PDFuserName," ", _PDFuserLast," ", _PDFuserNum," ", _PDFfileType)
                # #time.sleep (500)
            else:
                print("se debe configurar esta parte")

  
            #_PDFname variable hace referencia al nuevo nombre CON la extencion del archivo original
            _PDFname='{}{}{}{}{}{}{}{}'.format( _PDFuserName,"_", _PDFuserLast,"_", _PDFuserNum,"_", _PDFfileType, file_extension)
            os.chdir(_dirPDF)
            print("\nel directorio de cambio de nombre es: ",os.getcwd())
            print("\nlos archivos son: ",os.listdir(os.getcwd()))
            try:
                os.rename(_filename, _PDFname)
            except PermissionError:
                print("se dio un error permiso de escritura: \"PermissionError\"")
                time.sleep(3000)
                os.rename(_filename, _PDFname)
            # finally:
            #     time.sleep(3)
            #     os.rename(_filename, _PDFname)
            
            if _convert2PDF==True and file_extension != ".PDF" and file_extension != ".pdf"  :
                _convertToPDF=True              
        return _convertToPDF
        

    def MoverPDF(self):
        print("\nEn Funcion << MoverPDF >> con PID# ",os.getpid())
        #_GetDomain es true o false
        _GETHostPCName=sysVar.Get("VarGetDomainName")
        _DestPCName=sysVar.Get("VarDestinyPC")
        _TXTHostPCName=sysVar.Get("VarHostPC")
        _destFOLDER=sysVar.Get("VarDestinyFOLDER")
        #_UnidadEnRED es true o false
        _UnidadEnRED=sysVar.Get("VarUndEnRED")
        _UseDate2Move=sysVar.Get("VarUseDate2Move")
        self.DirChangeDetect()
        MngObj.ShowObjectsListaBefore()
        AA=MngObj.GET_ListaAfter()
        
        if _UnidadEnRED==True:
                    if _GETHostPCName==True:
                        _GETTXTHostPCName=socket.gethostname()
                        N=_GETTXTHostPCName
                    else:
                        N=_TXTHostPCName

                    print("variable para uso fecha ",_UseDate2Move)
                    if _UseDate2Move == True:
                        print("entre en el true con fecha")
                        formato = '%m-%d-%y'  # establece formato de fecha-hora podria ser '%d-%m-%y %H:%M:%S' 
                        _fecha=datetime.fromtimestamp(time.time()).strftime(formato)
                        T="{}{}".format("_",_fecha)   
                    else: 
                        T=""
                    _variable="{}{}".format(N,T)
                    print(_variable)
                    _dir="{}{}{}".format(_destFOLDER,"/",_variable)
                    try:
                        os.makedirs(_dir)
                    except:
                        print("se genero un error creando el directorio")
                        print("el directorio ya existe!!!")
                    finally:
                        for f in AA:
                            print("mover << ",f," >> a << ",_dir," >>")
                            shutil.move(f,_dir)
                            MngObj.CLEARListaObjBE()
        else:
            print ("se debe de establecer un socket")
             #MngObj.CLEARListaObjBE()

