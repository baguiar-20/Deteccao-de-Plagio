#include <stdio.h>

int main() {
	int matriz [100][100];
	int lin , col ,n;
	
	scanf("%d", &n);
	
	for(lin = 1; lin <= n; lin++){
		for(col = 1; col<= n; col++)
		   scanf("%d",&matriz[lin][col]);
	}
	
	 for(lin = 1; lin <= n; lin++){
		for(col = 1; col <= n; col++){
		    if (lin == col){
			   printf("%d ", matriz[lin][col]);
			}
	     }
	 }    
  return 0;		   
}
		
	
		
	
	
