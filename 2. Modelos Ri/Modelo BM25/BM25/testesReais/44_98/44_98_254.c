#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N 1000

int main()
{
	int i, j, n, mat[N][N];
	
	//printf("Digite a ordem da matrix: ");
	scanf("%d", &n);
	
	for(i=0; i<n; i++)
	{
		for(j=0; j<n; j++)
		{
			scanf("%d", &mat[i][j]);
		}	
	}
	
	for(i=0; i<n; i++)
	{
		printf("%d \t", mat[i][i]);
	}
	
	



	return 0;
}
