#include <stdio.h>
void main()
{
    int arr[5];
    int arr2[5];
    int arr1[5];
    int i;
    int sum = 0;
    for (i = 0; i < 5; i++)
    {
        printf("enter a number first number %d", i);
        scanf("%d", &arr1[i]);
    }
    for (i = 0; i < 5; i++)
    {
        printf("enter the second number %d   ", i);
        scanf("%d", &arr2[i]);
    }
    for (i = 0; i < 5; i++)
    {
        arr[i] = arr2[i] * arr1[i];
    }
    for (i = 0; i < 5; i++)
    {
        printf("\n%d", arr[i]);
    }
}
