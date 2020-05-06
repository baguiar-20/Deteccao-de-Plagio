#include <stdio.h>
int main (){
	int matrizA[10][10];
	int i,j,num;
	
	do{
	//printf ("Entre com a dimensao da matriz: \n");
	scanf ("%d",&num);
	}while (num<0);
	//printf ("Digite os elementos da matriz A: \n");
	for (i=0;i<num;i++) {
    	for (j=0;j<num;j++) {
        	scanf("%d" , &matrizA[i][j]);
        }
        printf("\n");
    }
    
    /*printf ("matriz A: \n");
    for (i=0;i<num;i++) {
    	for (j=0;j<num;j++) {
        	printf("%d" , matrizA[i][j]);
        	printf(" " );
        }
        printf("\n");
    }
    printf ("Imprimi os valores da diagonal principal: \n");*/
    for (i=0;i<num;i++) {
    	for (j=0;j<num;j++) {
			if (i==j){
        	printf("%d" , matrizA[i][j]);
        	printf(" " );
		}
        }        
    }
    
	return 0;
}
