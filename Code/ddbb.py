
# to do: hacer que las listas se llenen en base a un txt
# pedir archivo con informacion en txt > parsearlo > pasarlo a una lista > retorna la informacion
# de momento asi como esta pasa la informacion segun la base, nada mas que la enlista las bases, no toma los nombres

def log():
     archivo = open('log.txt','r')
     lista_log = list()
     for line in archivo:   
          x = line.replace('\n','')
          x = lista_log.append(x)
     print('Lista parseada de logs')
     return lista_log

def not_log():
     archivo = open('not_log.txt','r')
     lista_not_log = list()
     for line in archivo:   
          x = line.replace('\n','')
          x = lista_not_log.append(x)
     print('Lista parseada de not_log')
     return lista_not_log

def errores():
     archivo = open('errores.txt','r')
     lista_errors = list()
     for line in archivo:   
          x = line.replace('\n','')
          x = lista_errors.append(x) 
     print('Lista parseada de errores')
     return lista_errors

def not_errors():
     archivo = open('not_errors.txt','r')
     lista_not_errors = list()
     for line in archivo:   
          x = line.replace('\n','')
          x = lista_not_errors.append(x)  
     print('Lista parseada de not_errors')
     return lista_not_errors


def db():
     log()
     not_log()
     errores()
     not_errors()
     return[log(),not_log(),errores(),not_errors()]

db()