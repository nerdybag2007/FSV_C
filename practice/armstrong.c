#include<stdio.h>
void main(){
    int n;
    int temp;
    int sum=0;
    int r;
    printf("entter a number");
    scanf("%d",&n);
    temp=n;
    while(n>0);{
    r=n%10;
    sum=sum+(r*r*r);
    n=n/10;


}
if(sum==temp){
    printf("armstrong");

}else{
    printf("not and armstrong");
}
}
