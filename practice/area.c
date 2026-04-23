#include<stdio.h>
void main(){
    char op;int a,b,area;
     printf("Choose operation (s=square, r=rectangle, c=circle, b=cube):");
    scanf("%c",&op);
    printf("enter two numbers");
    scanf("%d%d",&a,&b);
    switch(op){
        case'z':area=6*(a*b); 
        scanf("%d",&a,&b);  
             printf("area of cube=%d",area);
             break;
        case's':area=a*a;
        scanf("%d,&a");
            printf("area of square=%d",area);
            break;
        case'r':area=a*a
        ;scanf("%d",&a);
            printf("area of rectangle=%d",area);
            break;
        case'c':area=3.14*(a*a);
        scanf("%d",&a);
             printf("area of circle=%d",area);
             break;
        default:printf("invalid");
    }
}