def db():
     log=["DEBUG","INFO","WARNING"]
     not_log = ["#####","<?xml","npreMemory.c{DEP}","npDrvPublEVT","npreFindClose","SendRecvTCPMsg","npreMsg.c{DEP}@2922","npreControlProcess.c{DEP}@149","npreOSItf.c{DEP}@796","npreOSItf.c{DEP}@254","ERROR","WARNING","N E W"]
     errors = ["ERROR","N E W ","WARNING","FATAL"]
     not_erros= ["ERROR_LOG","Error de comunicacion","Error executing command","npreFindClose","SendRecvTCPMsg resource","InsertResource resource","WARNING_LOG","COD0028","npreMsg2_SendRecvEx","GetResource:","Configuration parameter","ChangeItemPriceBySaleType","PosShowPrice","PosDoTryGrillEnd","cPosCheckPromotedOrder","PosConvertProduct","The Offers Server took more","sharpmessaging.cpp{DEP}@225","npreMemory.c","npDrvPublEVT.c"]
     return[log,not_log,errors,not_erros]