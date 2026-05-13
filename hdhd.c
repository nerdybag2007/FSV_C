#include <stdio.h>
void main()
{
    int n = 10;
    int i, j, minindex, temp, arr[n], key, uniqueindex;
    for (i = 0; i < n; i++)
    {
        printf("enter the array nigga");
        scanf("%d",&arr[i]);
    }
    for (i = 0; i < n - 1; i++)
    {
        minindex = i;
        for (j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[minindex])
            {
                minindex = j;
            }
        }
        if (minindex != i)
        {
            temp = arr[i];
            arr[i] = arr[minindex];
            arr[minindex] = temp;
        }
    }
    printf("\nafter sorting array we get");
    
    printf("enter a number");
    scanf("%d", &key);

    int s = 0, e = n - 1, mid, found = 0;
    while (s <= e)
    {

        mid = s + (e - s) / 2;
        if (arr[mid] == key)
        {
            printf("your value is found on index   %d", mid);
            found = 1;
            break;
        }
        else if (key < arr[mid])
        {
            e = mid - 1;
        }
        else
        {
            s = mid + 1;
        }
    }
    if (found == 0)
    {
        printf("bye");
    }
}