#include<stdio.h>
void main(){
int i,n,a=0,b=1,sum;
printf("enter the number of terms");
scanf("%d",&n);
sum=a+b;
a=b;
b=sum;
for(i=1;i<=n;i++){
    printf("%d",a);
    sum=a+b;
a=b;
b=sum;
    

}
}
//fibbonaci series