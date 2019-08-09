# simple script to convert pdf file into separate png images

'''
Dependencies
=============
-> Upgrade pip
        pip install pip --upgrade
-> install wand
        pip install wand
-> install PyPDF2
        pip install pypdf2
(I think that's it. But, if you have any problems, install the following too!)
*installed them in previous trials*
-> install ImageMagick , Ghostscript  >>> .exe   32-bit
        GhostScript : http://downloads.ghostscript.com/public/
        ImageMagick : https://wiki.python.org/moin/ImageMagick
'''


'''
HOW to use
===========
-> call convert(p1 , p2)
        p1 is a str = file name without .pdf
        p2 is optional -> int = resolution in dpi required
-> you can import this module in any script as usual
        from pdf2png import convert
'''

import PyPDF2

import io
import os

from wand.api import library
from ctypes import c_void_p, c_size_t
# Tell Python's wand library about the MagickWand Compression Quality (not Image's Compression Quality)
library.MagickSetCompressionQuality.argtypes = [c_void_p, c_size_t]

from wand.image import Image

'''
# source of pdf files
# set the directory absolute path .. 1- cd to whatever dir you want
                                     2- open python shell
                                     3- run os.path.abspath(os.getcwd())  this'll return the absolute path

'''
from system_var import *

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




class pdf2png():
        print("\nEn Funcion  <<< pdf2png >>> con PID# ",os.getpid())
        _dirPDF=sysVar.Get("VarDirPDF")
        #os.chdir(_dirPDF)


        dir_abs_path=_dirPDF  # example
        print("dir_abs_path es: ",dir_abs_path)
        # optional : set a different dir to save to
        # by default it will save to same dir of the pdf

        _Instdir=sysVar.Get("VarInstalationDir")
        _Ldir="{}{}".format(_Instdir,"/imagenes/thumb/")

        #>>> HACER _MultiPage True para que esta funciones convierta todas las paginas del archivo a PNG
        _MultiPage=False

        #os.chdir(_Ldir)
        save_abs_path = _Ldir
        print("save_abs_path es: ",save_abs_path)

        def pdf_page_to_png(self, src_pdf, pagenum = 0, resolution = 50):
                '''
                Returns specified PDF page as wand.image.Image png.
                :param PyPDF2.PdfFileReader src_pdf: PDF from which to take pages.
                :param int pagenum: Page number to take.
                :param int resolution: Resolution for resulting png in DPI.
                '''
                # print("ENTRE EN EL pdf_page_to_png ")
                # dst_pdf = PyPDF2.PdfFileWriter()
                # dst_pdf.addPage(src_pdf.getPage(pagenum))

                # pdf_bytes = io.BytesIO()
                # dst_pdf.write(pdf_bytes)
                # pdf_bytes.seek(0)
                # bg_colour = "#ffffff"
                # img = Image(file= pdf_bytes, width=75, height=75, background= bg_colour, resolution= resolution)
                # img.convert("png")

                # return img

                # Example of converting exam.pdf located at the same direcory
                # convert('exam')   # NOTE : default resolution is 72 dpi

        def convert2png(self, pdf_name, _filePNG, _filePNG2, resolution=72):
                '''
                Saves each page from a specified PDF as a png image (pdf_name{page_index}.png)
                :param str pdf_name : PDF file name (in the same directory of this script)
                :param int resolution : resolution of the output png_s in DPI
                '''
                print("el valor de pdf_name en convert es : ",pdf_name)
                print("entre en el CONVERT")
                # src_pdf = PyPDF2.PdfFileReader(open(os.path.join(self.dir_abs_path,pdf_name), "rb"))
                # for i in range(src_pdf.getNumPages()):
                #     if self._MultiPage==True:
                #         temp=self.pdf_page_to_png(src_pdf,i,resolution)
                #         temp.save(filename=os.path.join(self.save_abs_path,pdf_name+str(i)+'.png'))
                #         final="{}{}{}{}".format("se creo el archivo <<< ",_filePNG," >>> en la carpeta: ", self.save_abs_path)
                #     else:
                #         if i == 0:
                #             temp=self.pdf_page_to_png(src_pdf,i,resolution)
                #             temp.save(filename=os.path.join(self.save_abs_path,_filePNG))
                #             final="{}{}{}{}".format("se creo el archivo <<< ",_filePNG," >>> en la carpeta: ", self.save_abs_path)

                # _file_="{}{}{}".format(self._Ldir,"/",_filePNG)
                # #COMPRIMIENDP IMAGEN GENERADA
                # with Image(filename=_file_) as img:

                #     # factor para redimencionar la imagen manteniendo proporcion de la misma
                #     o_size = img.size   #Tamaño original de la imagen
                #     f_size = (256, 256) #Tamaño o proporcion final a la que se desea quede la imagen

                #     factor = min(float(f_size[1])/o_size[1], float(f_size[0])/o_size[0])
                #     width = int(o_size[0] * factor)
                #     height = int(o_size[1] * factor)
                    
                #     img.resize(width=width, height=height)

                #     # Set the optimization level through the linked resources of 
                #     # the image instance. (i.e. `wand.image.Image.wand`)
                #     library.MagickSetCompressionQuality(img.wand, 75)

                #     img.save(filename=os.path.join(self.save_abs_path,_filePNG2))
                #     os.remove(os.path.join(self.save_abs_path,_filePNG))
                
                # return final


if __name__== "__main__":
        print("entre en el if")
        x=pdf2png()
        a="t.pdf"
        b="t.png"
        c="t2.png"
        R=x.convert2png(a,b,c,90) 
        print(R)