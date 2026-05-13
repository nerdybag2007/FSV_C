#include <stdio.h>
void main()
{
    int n = 3
    ;
    int i, j;
    int arr[n][n];

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("Enter %d %d value\t", i, j);
            scanf("%d", &arr[i][j]);
        }
    }
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        

            {
                printf("%d", arr[i][j]);
            }
            printf("\n");
        }
    }
