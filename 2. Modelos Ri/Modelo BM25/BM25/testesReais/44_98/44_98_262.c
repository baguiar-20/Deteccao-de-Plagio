#include <stdio.h>

int main(int argc, char **argv)
{
	int n, mat[1000][1000], i, j;
	scanf ("%d", &n);
	for (i=0;i<n;i++) {
		for (j=0;j<n;j++) {
		scanf ("%d", &mat[i][j]);
	}
}
    for (i=0;i<n;i++) {
		for (j=0;j<n;j++) {
	    if (i==j) {
			printf ("%d ", mat[i][j]);
		}
	}
}
		
	return 0;
}

