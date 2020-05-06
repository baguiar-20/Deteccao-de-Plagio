#include <stdio.h>
int main (){
	int a[10][10];
	int i,j,n;
	
	do{
	scanf ("%d",&n);
	}while (n<0);
	for (i=0;i<n;i++) {
    	for (j=0;j<n;j++) {
        	scanf("%d" , &a[i][j]);
        }
        printf("\n");
    }
    for (i=0;i<n;i++) {
    	for (j=0;j<n;j++) {
			if (i==j){
        	printf("%d" , a[i][j]);
        	printf(" " );
		}
        }        
    }    
	return 0;
}
