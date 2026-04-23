#include<stdio.h>
void main(){
    //===================================== VD ==============================
    int a,b,c;
    printf("Enter a b and c");
    scanf("%d%d%d",&a,&b,&c);

    //====================================== LOGIC ==============================
    if(a>b){
        if(a>c){
            printf("A is greatest");
        }
    }else if(b>c){
        printf("B is greatest");
    }else{
        printf("C is greatest");
    }
}