#include<stdio.h>
void vote(int age){

if(age>=18){
    printf("elidgible to vote");
}else{
    printf("inedlidgibe to vote");
}
}
void main(){
    int n;
    printf("enter your age");
    scanf("%d",&n);
    vote(n);
}



