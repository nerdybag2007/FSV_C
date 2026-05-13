#include <stdio.h>
void main()
{
    int n = 3;
    int i, j, k, mul = 1;
    int arr[n][n], arr1[n][n], arr2[n][n];
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("enter number");
            scanf("%d", &arr[i][j]);
        }
    }

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            mul = mul * arr[i][j];
        }
    }

    printf("%d", mul);
}