#include <stdio.h>
#include <stdlib.h>

int main(){
 int i=0,n,linha=0,coluna=0; 
 scanf("%d",&n);
 int m[n][n];
 while(coluna<n){
	 while(linha<n){
		 scanf("%d",&m[coluna][linha]);
		 linha++;
	 }
	 linha=0;
	 coluna++;
 }
 while(i<n){
	 printf("%d ", m[i][i]);
	 i++;
 }
 
 return 0;
 
}
