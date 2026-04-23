#include<stdio.h>

int main(){
    int a;
    int b; 
    printf("enter two numbers");
    scanf("%d%d",&a,&b);
    (a<b)?printf("b is greater than a"):printf("a is obviously greater than b");
    return 0;
}