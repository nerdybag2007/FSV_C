#include <stdio.h>
void main()
{
    int j, i, n,s=1,y;
    printf("enter a number");
    scanf("%d", &n);
    if(n==1||n==2){
        printf("n is small for a box new n = 3");
        n=3;
    }
    else if(n%2==0){
        printf("ur n is even incrementing it to next odd");
        n++;
    }

    for (i = 1; i <= n; i++)
    {
        for (j = 1; j>=n; j++){
    }
        printf("\n");
    }
}