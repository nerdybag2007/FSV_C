#include <stdio.h>

void main()
{
    int n = 8;
    int arr[n], i, j, temp, minIndex;
    
    
    for (i = 0; i < n; i++)
    {
        printf("Enter array index %d \t", i);
        scanf("%d", &arr[i]);
    }
    
    
    printf("\noriginal array: ");
    for (i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    
    
    for (i = 0; i < n - 1; i++)
    {
        minIndex = i;
        
        for (j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[minIndex])
            {
                minIndex = j;
            }
        }
        
        if (minIndex != i)
        {
            temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }
    
    
    printf("\nafter sorting array: ");
    for (i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    
    printf("\n");
}