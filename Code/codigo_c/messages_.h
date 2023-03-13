#include "stdlib.h"
#include "stdio.h"
#include "colour_.h"

#define MSG_C_ERROR 0 
#define MSG_C_WARNING 1
#define MSG_C_INFO 2

const char *get_message (int evt_msg, int i_msg);
void printf_msg_c(int e, char *s);
/*---------------------------------------------------------------------------*/
/*
const char *get_message (int evt_msg, int i_msg)
{
	const char *msg_1[4] = {	"[OK  ] TPA\tINIT/EOF",
								"[FAIL]     : INICIO/FIN TPA | Sin evento 997 (Fin de Archivo TPA)",
								"[FAIL]     : INICIO/FIN TPA | Cantidades incorrectas de eventos de Inicializacion y Fin de Archivo TPA",
								"[FAIL]     : INICIO/FIN TPA | Sin eventos de Inicializacion y Fin de Archivo TPA",
								};
	const char *msg_2[3] = {	"[OK  ] SHIFTS\tOPEN/CLOSE",
								"[FAIL]     : APERTURAS/CIERRES TURNOS | Falta evento 72 de Cierre de algun Turno",
								"[FAIL]     : APERTURAS/CIERRES TURNOS | Cantidades incorrectas de eventos de Apertura y Cierre de Turnos"
								};
	const char *msg_3[3] = {	"[OK  ] DAY\tOPEN/CLOSE",
								"[FAIL]     : APERTURA/CIERRE DIA | Falta evento 71 de Cierre de Dia",
								"[FAIL]     : APERTURA/CIERRE DIA | Cantidades incorrectas de eventos de Apertura y Cierre de Dia"
								};
								
	switch(evt_msg)
	{
		case 1: { return msg_1[i_msg]; break; }
		case 2: { return msg_2[i_msg]; break; }
		case 3: { return msg_3[i_msg]; break; }
		break;
	}
}
*/
/*---------------------------------------------------------------------------*/
const char *get_message (int evt_msg, int i_msg)
{
	const char *msg_1[4] = {	"[OK  ] TPA\tINIT/EOF",
								"[FAIL] TPA\tINIT/EOF   | Sin evento 997 (Fin de Archivo TPA)",
								//"[FAIL] TPA\tINIT/EOF Cantidades incorrectas de eventos de Inicializacion y Fin de Archivo TPA",
								"[FAIL] TPA\tINIT/EOF   | Cantidades de eventos de TPA (998, 997)",
								"[FAIL] TPA\tINIT/EOF   | Sin eventos de Inicializacion y Fin de Archivo TPA"
								};
	const char *msg_2[3] = {	"[OK  ] DAY\tOPEN/CLOSE",
								"[FAIL] DAY\tOPEN/CLOSE | Falta evento 71 de Cierre de Dia",
								"[FAIL] DAY\tOPEN/CLOSE | Cantidades de eventos de Dia (70, 71)"
								};
								
	const char *msg_3[3] = {	"[OK  ] SHIFTS\tOPEN/CLOSE",
								"[FAIL] SHIFTS\tOPEN/CLOSE | Falta evento 72 de Cierre de algun Turno",
								//"[FAIL] SHIFTS\tOPEN/CLOSE | Cantidades incorrectas de eventos (Apertura, Cierre) de Turnos"
								"[FAIL] SHIFTS\tOPEN/CLOSE | Cantidades de eventos de Turnos (90, 72)"
								};
								
	switch(evt_msg)
	{
		case 1: { return msg_1[i_msg]; break; }
		case 2: { return msg_2[i_msg]; break; }
		case 3: { return msg_3[i_msg]; break; }
		break;
	}
}
/*---------------------------------------------------------------------------*/

void printf_msg_c(int e, char *s)
{
	switch(e)
	{
		case 0:{
			Color(BLACK, LRED);
			break;
		}
		case 1:{
			Color(BLACK, YELLOW);
			break;
		}
		case 2:{
			Color(BLACK, LGREEN);
			break;
		}
		default:
			Color(BLACK, e);
		break;
	}
	
	printf(s);
	RESET_COLOUR	
}
/*---------------------------------------------------------------------------*/

						
						
