/**
 * UNIVERSIDADE FEDERAL DO AMAZONAS
 * INSTITUTO DE COMPUTACAO
 *
 * Disciplina: Algoritmos e Estrutura de Dados (AED I)
 * Programa:   "Matriz diagonal"
 * Objetivo:   Imprimir os termos da diagonal principal
 * Autor:      Lazaro Junior Machado Pontes
 */

#include <stdio.h>
#include <stdlib.h>

int main()
{
	
	int mat[100][100]; 
	int n;			       
	int i, j;			      

	
		scanf("%d",&n);
		

		for (i=0; i<n; i++) {
			for (j=0; j<n; j++){
				scanf("%d",&mat[i][j]);
			}
		}
			
	
	for (i=0; i<n; i++) {
		for (j=0; j<n; j++) {
			if (i == j)            
				printf("%d \n",mat[i][j]);
		}
	}

	

	
	
	
	return 0;
}
