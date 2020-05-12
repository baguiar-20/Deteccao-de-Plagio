//
//  main.c
//  DP_matriz
//
//  Created by Ligia Freitas on 10/08/13.
//  Copyright (c) 2013 Ligia Gonçalves de Freitas. All rights reserved.
//

#include <stdio.h>

int main()
{
    int ordem, i, j;
    scanf("%d", &ordem);
    
    int mat[ordem][ordem];

    for (i=0; i < ordem; i++)
    {
        for (j=0; j < ordem; j++)
        {
            scanf("%d", &mat[i][j]);
        }
    }
    
    for (i=0; i < ordem; i++)
    {
        for (j=0; j < ordem; j++)
        {
            if (i == j)
            {
                printf("%d ", mat[i][j]);
            }
        }
    }
    return 0;
}

