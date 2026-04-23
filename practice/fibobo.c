#include<stdio.h>
int main(){
    int a=0,b=1,c,i=1,n;
    printf("enter a number");
    scanf("%d",&n);
    printf("%d %d",a,b);
    while (i<=n-2)
    {
        c=a+b;
        a=b;
        b=c;
        printf("%d ",c);
        i++;
    }
    return 0;
    
}
