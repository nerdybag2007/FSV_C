#include <stdio.h>
void main()
{
    int j, i, n;
    printf("enter a number");
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j>=n; j++){
        if (i==1||i==n||j==1||j==n||i+j==n+1)
        {
            printf("0");
            
        }else{
            printf(" ");
        }
    }
        printf("\n");
    }
}