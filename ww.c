#include<stdio.h>
void main(){
    int i,j,n;
    printf("enter a number");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            if(i==1||i==n||j==1||j==n){
                printf("%d%d",i,j);
            }else{
                printf(" ");
            }
        }
        printf("\n");
    }


}