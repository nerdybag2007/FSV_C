#include<stdio.h>
void main(){
    char op;
    int a , b, sum,mul;
    printf("enter a operatio");
    scanf("%c",&op);
    printf("enter two numbers");
    scanf("%d%d",&a,&b);

        switch(op){
            case '+': sum = a + b;
                        printf("Sum = %d",sum);
                    break;
            case '-': mul = a*b;
            printf(");
                    break;
            case 3: printf("WEDNESDAY");
                    break;
            case 4: printf("THURSDAY");
                    break;
            case 5: printf("FRIDAY");
                    break;
            case 6: printf("SATURDAY");
                    break;
            default: printf("invalid number");
    }
}