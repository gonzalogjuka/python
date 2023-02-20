def log():
     archivo = open('log.txt','r')
     lista_log = list()
     for line in archivo:   
          x = line.replace('\n','')
          x = lista_log.append(x)
     return lista_log

def not_log():
     archivo = open('not_log.txt','r')
     lista_not_log = list()
     for line in archivo:   
          x = line.replace('\n','')
          x = lista_not_log.append(x)
     return lista_not_log

def log_marc():
     archivo = open('marcador_log.txt','r')
     lista_marcadora = list ()
     for line in archivo:
          x = line.replace('\n','')
          x = lista_marcadora.append(x)
     return lista_marcadora

def errores():
     archivo = open('errores.txt','r')
     lista_errors = list()
     for line in archivo:   
          x = line.replace('\n','')
          x = lista_errors.append(x) 
     return lista_errors

def not_errors():
     archivo = open('not_errors.txt','r')
     lista_not_errors = list()
     for line in archivo:   
          x = line.replace('\n','')
          x = lista_not_errors.append(x)  
     return lista_not_errors

def error_marc():
     archivo = open('marcador_errores.txt','r')
     lista_marc_error = list ()
     for line in archivo:
          x = line.replace('\n','')
          x = lista_marc_error.append(x)
     return lista_marc_error

def base_links():
     archivo = open('confluence_links.txt','r')
     lista_confluence_links = list ()
     for line in archivo:
          x = line.replace('\n','')
          x = lista_confluence_links.append(x)
     return lista_confluence_links

def db():
     log()               # base 0
     not_log()           # base 1
     errores()           # base 2
     not_errors()        # base 3
     log_marc()          # base 4
     error_marc()        # base 5  
     base_links()        # base 6
     return[log(),not_log(),errores(),not_errors(),log_marc(),error_marc(),base_links()]

