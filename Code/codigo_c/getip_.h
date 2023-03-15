#include "stdlib.h"
#include "stdio.h"
#include "string.h"

//#define ESPERAR scanf("%*c");

void get_ip(char * ip);
void get_ip_3oct(char * ip, char * ip3oct);
int file_opem(FILE **file, const char *dir, const char *modo);
/*---------------------------------------------------------------------------*/
/*
int main(int argc, char **argv) 
{
	char data[100];
	char data_3oct[100];
	// xxx.xxx.xxx.xxx
	get_ip(data);
	printf("data: [%s]\n", data);
	
	get_ip_3oct(data, data_3oct);
	printf("data_3oct: [%s]\n", data_3oct);
	//printf("\npost data: [%s]\n", data);
	return (1);
}
*/
/*---------------------------------------------------------------------------*/
void get_ip_3oct(char * ip, char * ip3oct)
{
	//char ip3oct[30];
	int i = 0;
	int count_delimit = 0;
	
	while(ip[i] != '\0' && count_delimit < 3)
	{
		if(ip[i] == '.')
		{
			count_delimit++;
		}
		ip3oct[i] = ip[i];
		i++;		
	}
	ip3oct[i - 1] = '\0';
	//printf("ip3oct: [%s]\n", ip3oct);
}
/*---------------------------------------------------------------------------*/
void get_ip(char * ip)
{
	FILE *file_input;
	char linea[100];
	char findstr[100];
	char ipaddress[100];
	int i = 0, j = 0;
	char name_file_input[30] = "temp_ipway.txt";
	char command_cmd[50] = "ipconfig > "; 
	char command_cmd_del[50] = "del "; 
	
	strcat(command_cmd, name_file_input);
	system(command_cmd);
	
	if(file_opem(&file_input, name_file_input, "r"))
	{
		while(fgets(linea, sizeof(linea), file_input) && strstr(linea, "IP Address") == NULL && strstr(linea, "IPv4") == NULL);
		strcpy(findstr, strchr(linea, ':'));	
		while(findstr[i] != '\0')
		{
			if(findstr[i] >= '0' && findstr[i] <= '9' || findstr[i] == '.')
			{
				ipaddress[j] = findstr[i];
				j++;	
			}
			i++;
		}
		ipaddress[j] = '\0';
		strcpy(ip, ipaddress);
		fclose(file_input);	
	}
	strcat(command_cmd_del, name_file_input);
	system(command_cmd_del);

}
/*---------------------------------------------------------------------------*/
int file_opem(FILE **file, const char *dir, const char *modo)
{
	if((*file = fopen(dir,modo)) == NULL)
	{
		printf("\n[ERROR] Intenando abrir el archivo. (inaccesible o no existe): \n");
		printf("\"%s\"\n", dir);
		//fflush(stdin);
		return 0;
	}
	return 1;
}
