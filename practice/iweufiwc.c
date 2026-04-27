#include<stdio.h>
void pattern(int n){
    int i,j;
    for(i=1;i<=n;i++){
        for(j=1;j<=i;j++){
            printf("%d",j);
        }
printf("\n");
    }
}
    void main(){
        int n;
        printf("enter n");
        scanf("%d",&n);
        pattern(n);
    }
