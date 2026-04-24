#include<stdio.h>
void main(){
    int temp,r,n,e=0,o=0;
    printf("enter a number");
    scanf("%d",&n);
     temp=n;
     while(n>0){
        r=n%10;
        if(r%2==0){
            e++;
        }else{
            o++;
        }
        n=n/10;
     }
     printf("%d has %d even digits and %d odd digits",temp,e,o);
}