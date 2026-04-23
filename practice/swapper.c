#include<stdio.h>
void main(){
    int a ;
    int b ;
    printf("enter a and b number");
    scanf("%d%d",&a,&b);
    a=a+b;
    b=a-b;
    a=a-b;
    printf("a=%d\nb=%d",a,b);
}