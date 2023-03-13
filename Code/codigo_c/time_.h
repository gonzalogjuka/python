#include "stdio.h"
#include "time.h"
#include "string.h"


void get_date(char *date);
/*---------------------------------------------------------------------------*/
/*
int main(int argc, char **argv) 
{
	char day[100];
	
	get_date(day);
	printf("day: [%s]\n", day);

	return (1);
}
*/
/*---------------------------------------------------------------------------*/
void get_date(char *date)
{
  // Tiempo actual
  time_t t = time(NULL);
  struct tm tiempoLocal = *localtime(&t);
  // El lugar en donde se pondrá la fecha y hora formateadas
  char fechaHora[70];
  // El formato. Mira más en https://en.cppreference.com/w/c/chrono/strftime
  //const char *formato = "%Y-%m-%d %H:%M:%S";
  const char *formato = "%Y%m%d";
  // Intentar formatear
  int bytesEscritos = strftime(fechaHora, sizeof fechaHora, formato, &tiempoLocal);
  
  if (bytesEscritos != 0) {
    // Si no hay error, los bytesEscritos no son 0
    strcpy(date, fechaHora);
  } else {
    date = NULL;
  }
}
/*---------------------------------------------------------------------------*/

