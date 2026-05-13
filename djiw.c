#include <stdio.h>
void main()
{
    int n = 2, i, j, k,sum=0;

    int arr1[n][n], arr2[n][n],arr3[n][n];
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("enter 1st array");
            scanf("%d",&arr1[i][j]);
        }
    }
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {

            printf("enter 2st array");
            scanf("%d",&arr2[i][j]);
        }
    }
    for (i = 0; i < n; i++)
    {

        for (j = 0; j < n; j++)
        {
            for (k = 0; k < n; k++){

           sum=sum+arr1[i][j]*arr2[i][j];
           
                     
        }
         arr3[i][j]=sum;
         sum = 0;
    }
}
 for (i = 0; i < n; i++)
    {

        for (j = 0; j < n; j++){
printf("%d  ",arr3[i][j]);
        }
        printf("\n");
    }
}
