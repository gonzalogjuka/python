

log=["DEBUG","INFO","WARNING"]
not_log = ["#####","<?xml","npreMemory.c{DEP}","npDrvPublEVT","npreFindClose","SendRecvTCPMsg","npreMsg.c{DEP}@2922","npreControlProcess.c{DEP}@149","npreOSItf.c{DEP}@796","npreOSItf.c{DEP}@254","ERROR","WARNING","N E W"]
errors = ["ERROR","N E W ","WARNING","FATAL"]
not_erros= ["npBusCompAdp.cpp@95","npUpdtUtil.cpp{DEP}@234","npreMsg.c{DEP}@1690","npreMsg.c{DEP}@1640","ERROR_LOG","Error de comunicacion","Error executing command","npreFindClose","SendRecvTCPMsg resource","InsertResource resource","WARNING_LOG","COD0028","npreMsg2_SendRecvEx","GetResource:","Configuration parameter","ChangeItemPriceBySaleType","PosShowPrice","PosDoTryGrillEnd","cPosCheckPromotedOrder","PosConvertProduct","The Offers Server took more","sharpmessaging.cpp{DEP}@225","npreMemory.c","npDrvPublEVT.c"]
#return[log,not_log,errors,not_erros]
# to do: hacer que las listas se llenen en base a un txt
# pedir archivo con informacion en txt > parsearlo > pasarlo a una lista > retorna la informacion
# de momento asi como esta pasa la informacion segun la base, nada mas que la enlista las bases, no toma los nombres

def db():
     archivo = open('log.txt','r')
     lista_errores = list()
     for line in archivo:
          x = lista_errores.append(line)
          print(lista_errores)


