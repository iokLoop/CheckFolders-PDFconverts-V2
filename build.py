from GEimport import *
from multiprocessing import Process, Queue
########################
#	IMPORTANDO FUNCIONES PROPIAS
#########################
from functions import *
from system_var import *

#from objetos_dir import *

#print (system_var.__file__)
# print("la variable __name__ en Built es  : ",__name__)
# print("la variable __file__ en Built es : ",__file__)
# #print("la variable __path__ en Built es : ",__path__)

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
Job=FunctionsClass()
MngObj=ManejarObjFile()
print("\nEn Funcion  <<< Build >>> con PID# ",os.getpid())
print("1. Cargando las variables de entorno del archivo de configuracion")
print("2. Opteniendo el estado original de la carpeta en directorios")
MngObj.GETStateFolder(sysVar.Get("VarDirPDF"),"BEFORE")
while 1:
	time.sleep (5)
	MngObj.CLEARListaObjAF()
	L=MngObj.GETListaObjAF()
	print("\n\n\n el valor de lista after luego de limpiarla es: >>> ",L)
	_change=Job.DirChangeDetect()
	#_list=MngObj.GET_ListaBefore()
	if _change == True :
		print("\nvalor de variable renombrar x script es: ",sysVar.Get("VarUseRenByScrypt"))
		print("\n3. Llamando la funcion << CambiarNombres >>")
		print("\nla lista BEFORE antes de cambiar nombres es: ",MngObj.GET_ListaBefore())
		_convertToPDF=Job.CambiarNombres(sysVar.Get("VarDirPDF"), sysVar.Get("VarConvertToPDF"))
		MngObj.CLEARListaObjBE()
		MngObj.GETStateFolder(sysVar.Get("VarDirPDF"),"BEFORE")
		print("\nla lista BEFORE despues de cambiar nombres es: ",MngObj.GET_ListaBefore())
		if _convertToPDF==True:
			print("\n4. Llamando la funcion de << ConvertToPDF >>")
			Job.ConvertToPDF(sysVar.Get("VarDirPDF"),sysVar.Get("VarImgMagickDir"))
		print("\n5. Llamando la funcion << MoverPDF >>")
		Job.MoverPDF()
	else:
		print("<<<<< nada que hacer  >>>>>")
