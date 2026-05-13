// Online C compiler to run C program online
#include <stdio.h>

void main()
{
    int n = 3;
    int i, j, sum = 0;
    int arr[n][n];

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("enter ");

            scanf("%d", &arr[i][j]);
        }
    }
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            if (i == j)
            {
                sum = sum + arr[i][j];
            }
        }
    }
    printf("%d", sum);
}