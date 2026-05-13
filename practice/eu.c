#include <stdio.h>
void sort(int arr[], int n)
{
    int i, j, temp, minIndex;

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
}

void printArray(int arr[], int n){
    int i;
    for(i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
}
void main()
{
    int n = 8;
    int arr[n], i, j;
    for (i = 0; i < n; i++)
    {
        printf("ENter array %d index \t", i);
        scanf("%d", &arr[i]);
    }
    printf("\noriginal array");
    printArray(arr,n);
    
    // SORTING FUNCTIO
    sort(arr, n);

    printf("\nafter sorting array");
    printArray(arr,n);
}
