#define UNIVERSIDADE "Pontifícia Universidade Católica do Rio Grande do Sul"
	// deve-se colocar entre aspas

#include <sdtio.h>
#include <conio.h>   // necessário para as funções clrscr e getch

void main (){
   clrscr();     // Limpa a tela
   printf("%s", UNIVERSIDADE); // Imprime o nome representado pela constante
   getch();      // espera que o usuário pressione uma tecla
}