#include<stdio.h>
void main(){
    int a;
    printf("enter the value of future/past year");
    scanf("%d",&a);
    if(a%4==0){
        printf("a is a leap year");
    }else{
         printf("a is not a leap year");
    }
}