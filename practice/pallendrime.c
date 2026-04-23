#include<stdio.h>
void main(){
    int n;
    int temp;
    int r;
    int sum=0;
    printf("enter a number");
    scanf("%d",&n);
    temp=n;
    while(n>0){r=n%10;
    sum=sum*10+r;
n=n/10;
}
if(sum==temp){
    printf("yes it is a palandrome");

}else{
    printf("not a palandrome");
}
}