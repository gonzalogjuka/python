/*---------------------------------------------------------------------------*/
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "unistd.h"
#include "windows.h"
//#include "colour_.h"
// uso de los colores, libreria "colour_.h"
		//Color(BLACK, LRED);
		//RESET_COLOUR	
#include "messages_.h"
#include "getip_.h"
#include "time_.h"

#define ESPERAR scanf("%*c");

//#define COMPILACION_LOCAL
#define DIRWAYTPA "D:\\newpos61\\posfiles\\logs\\tlog"
// path (en WAY). "WAY D:\newspos61\posfiles\logs\tlog\"
// directorio POS/NGK. "POS00XX"
// nombre del archivo (en WAY). POS00XX_YYYYMMDD.tpa"

// path (en POS/NGK). "E:\newspos61\posfiles\logs\"
// nombre del archivo (en POS/NGK) npevt acual. npevt_POS00XX.tpa"
// nombre del archivo (en POS/NGK) npevt fecha. npevt_POS00XX_YYYYMMDD.tpa"
// nombre del archivo (en POS/NGK) nptrx acual. nptrx_POS00XX.tpa"
// nombre del archivo (en POS/NGK) nptrx fecha. nptrx_POS00XX_YYYYMMDD.tpa"

#define LONG_LINE_TPA 512
#define MAX_LINE_READ LONG_LINE_TPA + 8
#define STRLEN_LINE_TPA LONG_LINE_TPA - 1

#define LINE_POS 1
#define LINE_TAM 7
#define POS_POS 9
#define POS_TAM 9
#define DATE_POS 17
#define DATE_TAM 19
#define EVENT_POS 55
#define EVENT_TAM 4
#define INFO_POS // sin definir aun la posicion de inicio para obtner la informacion del comando
#define INFO_TAM 64

#define STRUCT_TAM 20

//#define MGS_INPUT_POS_NUMBER "Numero de POS, formato XXXX, ej.: 0020\n: "
#define MGS_INPUT_POS_NUMBER "Numero de POS/NGK\t:"
//#define MGS_INPUT_BUSINESS_DAY "Fecha de Negocio, formato YYYYMMDD, ej.: 20220531\n: "
#define MGS_INPUT_BUSINESS_DAY "Fecha, YYYYMMDD\t0:Actual:"

#define MGS_INPUT_4OCT "IP, x.x.x.999\t0:Way\t:"
#define MSG_ERROR_DATA_INPUT "\n[ERROR]: \"Numero de POS\" o \"Fecha de Negocio\" invalidos\n Ingresar los datos nuevamente\n\n"




typedef struct
{
	char ev_line[LINE_TAM];
	char ev_pos[POS_TAM];
	char ev_datetime[DATE_TAM];
	char ev_event[EVENT_TAM];
	char ev_info[INFO_TAM];	
}	st_event;

/*---------------------------------------------------------------------------*/

int AbrirArch(FILE **file, const char *dir, const char *modo);
int read_tpa(const char *name_file_input, st_event *evnt);
void get_event (const char *line, char *r_evento);
int find_event (const char *line, char *r_evento);
int is_event(const char* ln);
int is_number(const char c);
int is_espace(const char c);

void struct_event_convert(const char *line, st_event *st);
void struct_event_print(const st_event st);
void struct_print(const st_event *st);
int analysis_997_998(const st_event *st);
int analysis_day(const st_event *st);
int analysis_shifts(const st_event *st);
int struct_event_count (const st_event *st, const char *evt);


const char *message_resuelt (int evt_analysis, int msg);

void get_fullpath(char p[], int size, char *pos, char *day, char *ip4, char *ipb);
int validate_pos(char *p);
int validate_date(char *p);
int validate_4oct(char *p);
void titulo_inicial(void);
void menu_inicial(void);
void set_data_input(const char * title, char *data_in);
void convert(char *str);
void init_event_st(st_event *evnt);
//void printf_msg_c(int e, char *s);
/*---------------------------------------------------------------------------*/
int main(int argc, char **argv) 
{
	st_event events[STRUCT_TAM] = {'\0'};
	int result1 = 0;
	int result2 = 0;
	int result3 = 0;
	char path[200] = ""; 
	int param_ok = 1;
	int data_input_ok = 0;
	
	char pos_number[5]; // XXXX (... de exister una POS con nuemeracion mayor a 99)
	char business_day[9]; //YYYYMMDD
	// -p XXXX -d YYYYMMDD
	char ip4oct[4]; //xxx (4to Octeto de la direcion IP del equipo (POS/NGK) a obtener el archivo .tpa
	char ipdata[100]; 
	char ipbase[20];
	
	int cTecla = 0;
	
	//Obtengo la linea de la IP usando internamente el comando ipconfig de Windows, guardo en "ipdata"
	get_ip(ipdata);
	//Obsento los 3 primeros OCtetos de la IP, guardo en "ipbase"
	get_ip_3oct(ipdata, ipbase);

	//Mientras "cTecla = getch()" no sea 27 (27 = Tecla ESC), sigue mostrando las opciones
	while(cTecla != 27 && cTecla != 3)
	{
		// muestra el titulo
		titulo_inicial();
		
		//obtine el valor que corresponde a la tecla del teclado
		cTecla = getch();
		
		// si la tecla es ENTER (valor: 13), entra y continua.
		if(cTecla == 13)
		{
			// Entra a soliciar el ingreso de datos (POS, FECHA)
			while(data_input_ok == 0)
			{
				//ingreso datos: POS y FECHA
				set_data_input(MGS_INPUT_POS_NUMBER, pos_number);
				set_data_input(MGS_INPUT_BUSINESS_DAY, business_day);
				set_data_input(MGS_INPUT_4OCT, ip4oct);
				fflush(stdin);
				
				
				//printf("validate_4oct(ip4oct): %d", validate_4oct(ip4oct));ESPERAR
				//Se valida la informacion ingresada (POS, FECHA) y se asigna a la variable "data_input_ok"
				data_input_ok = validate_pos(pos_number) * validate_date(business_day) * validate_4oct(ip4oct);
				
				// si alguna de las validaciones (POS, FECHA) retorna 0, se mostrrá el mensaje de error
				// y volver a soliciar el ingreso de los datos (POS, FECHA). while
				if(data_input_ok == 0)
				{
					// muestra el mensaje de error con un color seteado
					printf_msg_c(MSG_C_ERROR, MSG_ERROR_DATA_INPUT);	
				}
			}
			
			//genero la path con el nombre del archivo segun los datos ingresados (POS, fecha)
			get_fullpath(path, sizeof(path), pos_number, business_day, ip4oct, ipbase);
			printf(" Archivo a procesar:...\n", path);
			printf(" [%s]\n", path);
			 
			// inicializa el array de structura st_event
			init_event_st(events);
			
			//lectura del tpa
			if(read_tpa(path, events))
			{
				printf("\n");
				
				//muestra la informacion leida
				struct_print(events);
				
				//ejcuta el analisis de los eventos
				
				result1 = analysis_997_998(events);
				//printf("result1: %d\n", result1);
				result2 = analysis_day(events);
				//printf("result2: %d\n", result2);
				result3 = analysis_shifts(events);
				//printf("result3: %d\n", result3);
				
				// muestra los mensajes segun los resultados de los analisis previos
				
				printf_msg_c(DGREY, "\n - Resultados: -\n");
				//printf ("\n - Resultados: -\n");
				//printf ("Archivo: %s\n", path);
				printf (" %s\n", message_resuelt (1, result1));
				printf (" %s\n", message_resuelt (2, result2));
				printf (" %s\n", message_resuelt (3, result3));				
			}
			data_input_ok = 0;
			strcpy(path, "");
			system("pause");
			printf("\n");
		}
	}
	return (1);
}

/*---------------------------------------------------------------------------*/
int AbrirArch(FILE **file, const char *dir, const char *modo)
{
	if((*file = fopen(dir,modo)) == NULL)
	{
		//printf("\nError al abrir archivo: \"%s\" , en modo: \"%s\"\n", dir, modo);
		printf_msg_c(0, "\n[ERROR] Intenando abrir el archivo. (inaccesible o no existe): \n");
		//printf_msg_c(0, dir);	 
		printf("\"%s\"\n", dir);
		printf("\n");
		//fflush(stdin);
		return 0;
	}
	return 1;
}

/*---------------------------------------------------------------------------*/
int read_tpa(const char *name_file_input, st_event *evnt)
{
	FILE *file_input;
	char linea[MAX_LINE_READ];
	char read_event[EVENT_TAM + 1] = "";
	//st_event list_event[20] = {'\0'};
	int i = 0;
	
	if(AbrirArch(&file_input, name_file_input, "r"))
	{
		while(fgets(linea, sizeof(linea), file_input))
		{	
		// obtengo en la variable 'read_event' el comando 
		// de la cadena 'linea' leida antes por fgets

		get_event(linea, read_event);
		
		//PROCESO SEGUN EL COMANDO
		if(	!strcmp(read_event, "998") ||
			!strcmp(read_event, "70 ") ||
			!strcmp(read_event, "90 ") ||
			!strcmp(read_event, "72 ") ||
			!strcmp(read_event, "71 ") ||
			!strcmp(read_event, "997") )
			{
				struct_event_convert(linea, &(evnt[i]));
				//struct_event_print(evnt[i]);
				i++;
			}
		}
		fclose(file_input);
		return 1;
	}
	else
		return 0;
}
 
/*---------------------------------------------------------------------------*/

void get_event (const char *line, char *r_evento)
{	
	if(is_event(line))
	{
		strncpy(r_evento, &line[EVENT_POS - 1], EVENT_TAM - 1);
		r_evento = '\0';
	}
	else
		r_evento[0] = '\0';
}

/*---------------------------------------------------------------------------*/
int find_event (const char *line, char *r_evento)
{	
	
	if(is_event(line))
	{
		if(	line[EVENT_POS - 1] == r_evento[0] &&
			line[EVENT_POS] == r_evento[1] &&
			line[EVENT_POS + 1] == r_evento[2] )
			return 1;
		else
			return 0;
	}
	else
		return 0;
}

/*---------------------------------------------------------------------------*/
int is_event(const char* ln)
{
	if(strlen(ln) == STRLEN_LINE_TPA)
	{
		if(is_number(ln[EVENT_POS - 1]))
		{
			if(is_number(ln[EVENT_POS]))
			{
				if(is_number(ln[EVENT_POS + 1]) || is_espace(ln[EVENT_POS + 1]))
					return 1;
				else
					return 0;
			}
			else
			{
				if(is_espace(ln[EVENT_POS]) && is_espace(ln[EVENT_POS + 1]))
					return 1;
				else
					return 0;	
			}
		}
		else
			return 0;
	}
	return 0;		
}

/*---------------------------------------------------------------------------*/
int is_number(const char c)
{
	return c != '\0' && c != ' ' && c >= 48 && c <= 57 ? 1 : 0;	
}

/*---------------------------------------------------------------------------*/
int is_espace(const char c)
{
	return c == ' ' ? 1 : 0;	
}

/*---------------------------------------------------------------------------*/
void struct_event_convert(const char *line, st_event *st)
{
	//obtiene los datos de la linea 'line' leida 
	//y los pasa a la estructura 'st'
	strncpy(st->ev_line, &line[LINE_POS - 1], LINE_TAM - 1);
	st->ev_line[LINE_TAM] = '\0';
	strncpy(st->ev_pos, &line[POS_POS - 1], POS_TAM - 1);
	st->ev_pos[POS_TAM] = '\0';
	strncpy(st->ev_datetime, &line[DATE_POS - 1], DATE_TAM - 1);
	st->ev_datetime[DATE_TAM] = '\0';
	strncpy(st->ev_event, &line[EVENT_POS - 1], EVENT_TAM - 1);
	st->ev_event[EVENT_TAM] = '\0';	
}

/*---------------------------------------------------------------------------*/
void struct_event_print(const st_event st)
{
	printf("%s | %s | %s | %s | %s\n", 
	st.ev_line, st.ev_datetime, st.ev_pos, st.ev_event, st.ev_info);
}

/*---------------------------------------------------------------------------*/
void struct_print(const st_event *st)
{
	int i = 0;
	
	// ARREGLAR LIMITE
	for(i; i < STRUCT_TAM && strcmp(st[i].ev_line, ""); i++)
	{
		struct_event_print(st[i]);
	}
}

/*---------------------------------------------------------------------------*/
int analysis_997_998(const st_event *st)
{
	int i = 0;
	int ret = -1; // valor de retorno
	
	int count_event_998 = 0;
	int count_event_997 = 0;
	
	count_event_998 = struct_event_count(st, "998");
	count_event_997 = struct_event_count(st, "997");
	
	if(count_event_998 == count_event_997 && count_event_998 == 1)
		ret = 0; // igual cantidad "Inicializacion" y "Cierres de Archivo TPA", ambos 1 vez. (OK)
	else
		if(count_event_998 > count_event_997 && count_event_998 == 1)
			ret = 1; // faltan el cierre de Archivo
		else
			ret = 2; // Extraño!. Existen cantidades incorrectas de "Inicializacion" y "Cierres de Archivo TPA"
			
	if(count_event_998 == 0 && count_event_997 == 0)
		ret = 3; // sin eventos de "Inicializacion" y "Cierres de Archivo TPA"
	
	return ret;
}

/*---------------------------------------------------------------------------*/

int analysis_day(const st_event *st)
{
	int i = 0;
	int ret = -1; // valor de retorno
	
	int count_event_70 = 0;
	int count_event_71 = 0;
	
	count_event_70 = struct_event_count(st, "70 ");
	count_event_71 = struct_event_count(st, "71 ");

	if(count_event_70 == count_event_71)
		ret = 0; // igual cantidad "Aperturas de Dia" y "Cierres de Dia" (OK)
	else
		if(count_event_70 > count_event_71)
			ret = 1; // faltan el cierre de dia (INFORMAR)
		else
			ret = 2; // Extraño!. Existen mas "Cierres de Dia" que "Aperturas de Dia"
	
	return ret;
}

/*---------------------------------------------------------------------------*/

int analysis_shifts(const st_event *st)
{
	int i = 0;
	int ret = -1; // valor de retorno
	
	int count_event_90 = 0;
	int count_event_72 = 0;
	
	count_event_90 = struct_event_count(st, "90 ");
	count_event_72 = struct_event_count(st, "72 ");

	if(count_event_90 == count_event_72)
		ret = 0; // igual cantidad de turnos abiertos y "Cierres de Turnos" (OK)
	else
		if(count_event_90 > count_event_72)
			ret = 1; // faltan Turnos por cerrar (INFORMAR).
		else
			ret = 2; // Extraño!. Existen mas "Cierres de Turnos" que "Aperturas de Turnos"
	
	return ret;
}

/*---------------------------------------------------------------------------*/
int struct_event_count (const st_event *st, const char *evt)
{
	int i = 0;
	int count = 0;
	
	for(i; i < STRUCT_TAM; i++)
		count += !strcmp(st[i].ev_event, evt);
	
	return count;
}

/*---------------------------------------------------------------------------*/
const char *message_resuelt (int evt_analysis, int msg)
{
	return get_message (evt_analysis, msg);
}
/*---------------------------------------------------------------------------*/
void get_fullpath(char p[], int size, char *pos, char *day, char *ip4, char *ipb)
{
	char today[20];
	
	//ejecucion local
	#ifdef COMPILACION_LOCAL
		getcwd(p, size);
		strcat(p, "\\");
		strcat(p, "POS");
		strcat(p, pos);
		strcat(p, "_");
		strcat(p, day);
		strcat(p, ".tpa");
	#else
	//ejecucion en produccion
		// Si el 4to Octeto (valor ingresado, ip4) es 0, entonces tomará el .tpa desde la WayStation
		// de lo contrario, toma el .tpa de equipo que se indicó (POS, 4to Octeto)
		if(strcmp(ip4, "0") == 0)
		{
			strcpy(p, DIRWAYTPA);
			strcat(p, "\\");
			strcat(p, "POS");
			strcat(p, pos);
			strcat(p, "\\");
			strcat(p, "POS");
			strcat(p, pos);
			strcat(p, "_");
			
			if(strcmp(day, "0") != 0)
			{
				//obtiene el archivo .tpa para la fecha indicada en la variable "day"
				strcat(p, day);	
			}
			else
			{	
				//obtiene el archivo .tpa para la fecha actual del sistema, variable "today"
				get_date(today);
				strcat(p, today);	
			}
			strcat(p, ".tpa");		
		}
		else
		{
			// Se arma el PATH para tomar el TPA desde la IP indicada
			strcat(p, "\\\\");
			strcat(p, ipb);
			strcat(p, ".");
			strcat(p, ip4);
			strcat(p, "\\");
			strcat(p, "e$");
			strcat(p, "\\newpos61\\posfiles\\logs\\");
			strcat(p, "npevt_");
			strcat(p, "POS");
			strcat(p, pos);
			
			// valido si la fecha ingresada es distinta de "0", entonces busco armo el path con la fecha de tpa ingresada
			// caso contrario, busco el tpa actual (sin fecha)
			if(strcmp(day, "0") != 0)
			{
				strcat(p, "_");
				strcat(p, day);	
			}
			strcat(p, ".tpa");	
			
		}
		//printf("\tp: [%s]\n", p); ESPERAR
	#endif
}
/*---------------------------------------------------------------------------*/
// valida que *p sea del formato 9999
// (4 digitos numericos)
int validate_pos(char *p)
{
	int tam_p;
	int i;
	int is_number = 1;
	
	convert(p);
	if(strcmp(p, "0000"))
	{
		tam_p = strlen(p);

		for(i = 0; i < tam_p && is_number == 1; i++)
			if(p[i] >= '0' && p[i] <= '9')
				is_number = 1;
			else
				is_number = 0;
		
		return (tam_p == 4 && is_number == 1) ? 1 : 0;
	}
	else
		return 0;

}
/*---------------------------------------------------------------------------*/
// valida que *p sea del formato YYYYMMDD
// (8 digitos numericos y una fecha válida)
int validate_date(char *p)
{
	int tam_p = strlen(p);
	int i;
	int is_number = 1;
	int format_number_ok = 0;
	
	char year[5] = "";
	char month[5] = "";
	char day[5] = "";
	
	int iyear, imonth, iday;
	
	for(i = 0; i < tam_p && is_number == 1; i++)
		if(p[i] >= '0' && p[i] <= '9')
			is_number = 1;
		else
			is_number = 0;
	
	// si tiene formato numero, 8 digitos nuemricos
	// continuo validando que sea una fecha.	
	if(tam_p == 8 && is_number == 1)
	{
		strncat(year, p, 4);
		iyear = atoi(year);
		
		strncat(month, p+4, 2);
		imonth = atoi(month);
		
		strncat(day, p+6, 2);
		iday = atoi(day);

		if((iyear > 2000 && iyear < 2040) && (imonth > 0 && imonth < 13) && (iday > 0 && iday < 32))
			return 1;
		else
			return 0;
	}
	else
	{
		if(!strcmp(p, "0"))
			return 1;
		else
			return 0;
	}
		
}
/*---------------------------------------------------------------------------*/
// valida que *p sea del formato 9999
// (4 digitos numericos)
int validate_4oct(char *p)
{
	int tam_p;
	int i;
	int is_number = 1;
	
	//convert(p);
	tam_p = strlen(p);

	for(i = 0; i < tam_p && is_number == 1; i++)
		if(p[i] >= '0' && p[i] <= '9')
			is_number = 1;
		else
			is_number = 0;
	
	return (tam_p < 4 && is_number == 1) ? 1 : 0;
}
/*---------------------------------------------------------------------------*/
void titulo_inicial(void)
{
	Color(BLACK, DGREY); 
	printf("-------------------------------------------------------------------------------\n"); 
	printf(" *** LECTURA DE ARCHIVO .TPA *** \n");
	printf("-------------------------------------------------------------------------------\n");
	RESET_COLOUR
	menu_inicial();
}
/*---------------------------------------------------------------------------*/
void menu_inicial(void)
{
	printf("\tENTER\t: Ingresar (POS, Fecha)\n");
	printf("\tESC\t: Salir\n\n");
}
/*---------------------------------------------------------------------------*/
void set_data_input(const char * title, char *data_in)
{
	int tecla;
	Color(LGREY, BLACK);
	printf("%s", title);
	RESET_COLOUR
	printf(" ");
	scanf("%s", data_in);
}
/*---------------------------------------------------------------------------*/
void convert(char *str)
{
	char aux[5] = "0000";
	int i;
	int tam_str = strlen(str);
	
	if(tam_str <= 4)
	{
		for(i = 0; i <= 4 && i <= tam_str; i++)
			aux[4 - i] = str[tam_str - i];
	}
	strcpy(str, aux);
}
/*---------------------------------------------------------------------------*/
void init_event_st(st_event *evnt)
{
	int i;
	for (i = 0; i < STRUCT_TAM; i++)
	{
		strcpy(evnt[i].ev_line, "");
		strcpy(evnt[i].ev_pos, "");
		strcpy(evnt[i].ev_datetime, "");
		strcpy(evnt[i].ev_event, "");
		strcpy(evnt[i].ev_info, "");
	}
}
/*---------------------------------------------------------------------------*/
