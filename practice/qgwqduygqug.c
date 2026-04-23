#include<stdio.h>
void main(){
    char op;
    int a,b,sum,mul,sub,div;
     printf("enter a operation");
    scanf("%c",&op);
    printf("enter two numbers");
    scanf("%d%d",&a,&b);
    switch(op){
        case '+':sum=a+b;
                printf("Sum = %d",sum);
               break;
        case '-':sub=a-b;
        printf("sub = %d",sub);
               ;break;
        case '*':mul=a*b;
        printf("mul = %d",mul);
               break;
        case '/':div=a/b;
        printf("div = %d",div);
               break;
    default:printf("invalid number");

    }
}