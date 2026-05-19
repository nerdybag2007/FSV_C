#include <stdio.h>
void main()
{
    int n,arr[20],i=0,j;
    printf("enter a number");
    scanf("%d", &n);
    while (n > 0)
    {
        arr[i]=n%2;
        
        

        
        n = n / 2;
        i++;
    }
    for(j=i-1;j>=0;j--){
        printf("%d",arr[j]);
    }
    
}