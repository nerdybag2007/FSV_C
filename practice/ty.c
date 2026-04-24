#include<stdio.h>
void main(){
    int sum=0,n,i,j,fact;
    printf("enter a number");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        fact=1;
        for(j=1;j<=i;j++){
            fact=fact*j;

        }
        sum=sum+fact;
    }
    printf("%d",sum);


}