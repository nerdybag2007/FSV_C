#include<stdio.h>
void main(){
    int j,i,n;
    printf("enter a number");
    scanf("%d",&n);
    for(i=1;i<=n;i++){

    
    for(j=1;j<=i;j++)
    {
printf("*",j);
    }
    printf("\n");
    }
}