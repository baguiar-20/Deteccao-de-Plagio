#include <stdio.h>
#include <stdlib.h>

int main(){
	int n;
	scanf("%d", &n);
	int matrix[n][n];	
	int linha, coluna;
	for (linha=0; linha<n; linha ++) for (coluna=0;coluna<n; coluna++) scanf("%d", &matrix[linha][coluna]);		
	for (linha=0; linha<n; linha ++) for (coluna=0;coluna<n; coluna++) if (linha==coluna) printf("%d ", matrix[linha][coluna]);		
return 0;
}
