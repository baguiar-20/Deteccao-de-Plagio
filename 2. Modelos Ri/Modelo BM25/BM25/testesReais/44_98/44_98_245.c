#include <stdio.h>

int main()
{
	int mat[10][10];
	int i, j, n;
	
	scanf("%d",&n);
	
	for(i=0; i<=n-1; i++){
		for(j=0; j<=n-1; j++){
			scanf("%d",&mat[i][j]);
		}
	}
	
	for(i=0; i<n; i++){
		for(j=0; j<n; j++){
			if (i==j)
				printf("%d ",mat[i][j]);
		}
	}
	
	
	
	
	return 0;
}

