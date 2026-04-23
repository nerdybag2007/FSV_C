#include<stdio.h>
void main(){
    int a;

    printf("enter your age please");
    scanf("%d",&a);
    (a<0)?printf("this age is invalid"):(a<18)?printf("inelidible to vote"):printf("elidible");

}