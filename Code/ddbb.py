def db():
     lista_log= ["DEBUG","INFO","WARNING"]
     lista_not_log= ["#####","<?xml","npreMemory.c{DEP}","npDrvPublEVT","npreFindClose","SendRecvTCPMsg","npreMsg.c{DEP}@2922","npreControlProcess.c{DEP}@149","npreOSItf.c{DEP}@796","npreOSItf.c{DEP}@254","ERROR","WARNING","N E W"]
     lista_errors= ["ERROR","N E W ","WARNING","FATAL"]
     lista_not_errors= ["npBusCompAdp.cpp@95","npUpdtUtil.cpp{DEP}@234","npreMsg.c{DEP}@1690","npreMsg.c{DEP}@1640","ERROR_LOG","Error de comunicacion","Error executing command","npreFindClose","SendRecvTCPMsg resource","InsertResource resource","WARNING_LOG","COD0028","npreMsg2_SendRecvEx","GetResource:","Configuration parameter","ChangeItemPriceBySaleType","PosShowPrice","PosDoTryGrillEnd","cPosCheckPromotedOrder","PosConvertProduct","The Offers Server took more","sharpmessaging.cpp{DEP}@225","npreMemory.c","npDrvPublEVT.c"]
     return[lista_log,lista_not_log,lista_errors,lista_not_errors]
# to do: hacer que las listas se llenen en base a un txt
# pedir archivo con informacion en txt > parsearlo > pasarlo a una lista > retorna la informacion
# de momento asi como esta pasa la informacion segun la base, nada mas que la enlista las bases, no toma los nombres

def log():
     archivo = open('log.txt','r')
     lista_log = list()
     for line in archivo:   
          x = line.replace('\n','')
          x = lista_log.append(x)    
     print(lista_log)

def not_log():
     archivo = open('not_log.txt','r')
     lista_not_log = list()
     for line in archivo:   
          x = line.replace('\n','')
          x = lista_not_log.append(x)    
     print(lista_not_log)

def errores():
     archivo = open('errores.txt','r')
     lista_errors = list()
     for line in archivo:   
          x = line.replace('\n','')
          x = lista_errors.append(x)    
     print(lista_errors)

def not_errors():
     archivo = open('not_errors.txt','r')
     lista_not_errors = list()
     for line in archivo:   
          x = line.replace('\n','')
          x = lista_not_errors.append(x)    
     print(lista_not_errors)

not_errors()