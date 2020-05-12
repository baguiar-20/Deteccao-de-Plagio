#include <stdio.h>

int main()
{
	int mat[1000][1000];
	int i,j,n;
	
	scanf ("%d",&n);
	
	for (i=1;i<=n;i++){
		for (j=1;j<=n;j++){
			scanf("%d",&mat[i][j]);
		}
	}
	
	for (i=1;i<=n;i++){
		for (j=1;j<=n;j++){
			if (i == j)
			printf ("%d ",mat[i][j]);
		}
	}
	
	return 0;
}

