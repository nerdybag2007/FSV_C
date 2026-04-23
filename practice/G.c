#include<stdio.h>
void main(){
    int n = 7;

    for(int i = 1;i<=n;i++){
        for(int j = 1;j<=n;j++){
            if(i==1||i==n||j==1||(j==n&&i>=(n+1)/2)||((i==(n+1)/2)&&j>=(n+1)/2))
            printf("* ");
            else
            printf("  ");
        }
        printf("\n");
    }
}