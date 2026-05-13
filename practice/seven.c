#include <stdio.h>
void main()
{
    int arr[5] = {5, 7, 2, 1, 8};
    int key;
    int i;
    int found = 0;
    while (1){
    printf("enter a number ");
    scanf("%d", &key);
    for (i = 0; i < 5; i++)
        {
            if (key == arr[i])
            {
                found = 1;
                printf("%d", i);
                break;
            }
        }
        if (found == 0)
        {
            printf("element not found");
        }
    }
}