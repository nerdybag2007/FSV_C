#include<stdio.h>
// without  arg and without return
// void multiplied(){
//     int a,b,c;
//     printf("enter a number");
//     scanf("%d",&a,&b);
//     c=a*b;
//     printf("multiplied=%d",c);

// }
// void main(){
//     multiplied();
// }
// void multiplication(int x,int y){
//     int c;
//     c=x*y;
//     printf("%d",c);

// }
// void main(){
//     int a,b;
//     printf("enter the number");
//     scanf("%d%d",&a,&b);
//     multiplication(a,b);
// }
//without return wit arg
// int multiplication(){
//     int a,b,c;
//     printf("ener a number");
//     scanf("%d%d",a,b);
//     c=a*b;
//     return c;
// }
// void main(){
//     int output;
//     output=multiplication();
//     printf("output",c);
// }without argument with retuen
int multiplication(int a,int b){
    int c=a*b;
    return c;

}
void main(){
    int a,b,out;
    printf("enter a number");
    scanf("%d%d",&a,&b);
    out=multiplication(a,b);
    printf("out=%d",out);
}