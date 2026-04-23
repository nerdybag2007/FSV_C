#include <stdio.h>
void main()
{
    //Declaration=====================================================================
    int j, i, n;
    //Scaning n=======================================================================
    printf("enter a number");
    scanf("%d", &n);
    //N chek===========================================================================
    if(n==1||n==2){
        printf("n is small for a box new n = 3\n");
        n=3;
    }
    else if(n%2==0){
        printf("ur n is even incrementing it to next odd\n");
        n++;
    }
    //patron logic=========================================================================
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j<=n; j++){
        if (i==1||i==n||j==1||j==n||i+j==n+1||i==j)
        {
            printf("0 ");
            
        }else{
            printf("  ");
        }
    }
        printf("\n");
    }
}