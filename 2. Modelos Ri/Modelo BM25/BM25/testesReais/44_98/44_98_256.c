#include <stdio.h>
 
int main(){
	int n, i, j;
	
	//printf("Informe a dimensao da Matriz Quadrada: ");
	scanf("%d", &n);
	
	int A[n][n];
	
	
	//printf("\nInforme os valores de matriz A:");
	for (i = 0; i < n; i = i + 1){
		for (j = 0; j < n; j = j + 1){
			scanf("%d", &A[i][j]);
		}
	}
		
	//printf("\n");
		
	for (i = 0; i < n; i = i + 1){
		for (j = 0; j < n; j = j + 1){
			if(i == j){
				printf("%d ", A[i][j]);
			}
		}
		//printf("\n");
	}
}
