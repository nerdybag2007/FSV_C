#include<stdio.h>
int main(){
    int n,i;
    printf("enter a number");
    scanf("%d",&n);
    i=1;
    while (i<=10)
    {
        
        i++;
        printf("%d*%d=%d",n,i,n*i);
    }
    return 0;
}