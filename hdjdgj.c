#include<stdio.h>
void main(){
    int a;
    printf("enter the value of no.");
    scanf("%d",&a);
    if((a%4==0)&&(a%7==0)){
        printf("a is divisble by 4and 7");
    }else{
         printf("a is noot divisible by4 and 7");
    }
}