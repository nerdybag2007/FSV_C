#include<stdio.h>
void main(){
    int i;
    int n;
    int sum=0;
    printf("enter the number");
    scanf("%d",&n);
    
    i=1;
    while(i<=n){
        printf("%d\n",i);
        sum=sum+i;
       i++;

    }
    printf("\nsum=%d\n",sum);

}