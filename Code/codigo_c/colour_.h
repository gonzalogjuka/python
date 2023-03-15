#include "stdlib.h"
#include "stdio.h"
#include "Windows.h"  // API del Sistema Operativo de Windows (Permite trabajar sobre la Consola).


#define RESET_COLOUR Color(BLACK, LGREY);
// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
void Color(int Background, int Text); // Prototipo de función           

enum Colors { // Listado de colores (La letra "L" al inicio, indica que es un color más claro que su antecesor).
	BLACK = 0,
	BLUE = 1,
	GREEN = 2,
	CYAN = 3,
	RED = 4,
	MAGENTA = 5,
	BROWN = 6,
	LGREY = 7,
	DGREY = 8,
	LBLUE = 9,
	LGREEN = 10,
	LCYAN = 11,
	LRED = 12,
	LMAGENTA = 13,
	YELLOW = 14,
	WHITE = 15
};
// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
/*
int main(){

	Color(BLACK, LGREEN);
	printf("Texto en color Verde Claro y fondo Negro");
	Color(BLACK, RED);
	printf("Texto en color Rojo y fondo Negro");
	Color(WHITE, BLACK);
	printf("Texto en color Negro y fondo Blanco");
	
	// Devolvemos el color original de la consola.
    Color(BLACK, WHITE); 
    printf("Volvimos a la normalidad!");
	
	return 0;
}
*/

void Color(int Background, int Text){ // Función para cambiar el color del fondo y/o pantalla

	HANDLE Console = GetStdHandle(STD_OUTPUT_HANDLE); // Tomamos la consola.

	// Para cambiar el color, se utilizan números desde el 0 hasta el 255.
	// Pero, para convertir los colores a un valor adecuado, se realiza el siguiente cálculo.
	int    New_Color= Text + (Background * 16); 

	SetConsoleTextAttribute(Console, New_Color); // Guardamos los cambios en la Consola.

}
