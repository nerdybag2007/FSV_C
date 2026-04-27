#include<stdio.h>
//=========================== WITHOUT ARUMENT & WITHOUT RETURN TYPE =================================
// void sum(){
    //     int a,b,c;
    //     printf("Enter a and b");
    //     scanf("%d%d",&a,&b);
    //     c = a + b;
    //     printf("Sum of a and b is %d",c);
    // }
    // void main(){
        //     sum();
        // }


//=========================== WITH ARUMENT & WITHOUT RETURN TYPE =================================
// void sum(int a, int b){
//     int c = a + b;
//     printf("Sum of two numbers is %d",c);
// }
// void main(){
//     int a, b;
//     printf("Enter a and b");
//     scanf("%d%d",&a,&b);
//     sum(a,b);
// }


//=========================== WITHOUT ARUMENT & WITH RETURN TYPE =================================
// int sum(){
//     int a, b, c;
//     printf("Enter a and b");
//     scanf("%d%d",&a,&b);
//     c = a + b;
//     return c;
// }
// void main(){
//     int out = sum();
//     printf("Sum of two numbers is %d",out);
// }


//=========================== WITH ARUMENT & WITH RETURN TYPE =================================
int sum(int x, int y){
    int c;
    c = x + y;
    return c;
}
void main(){
    int a , b;
    printf("Enter a and b");
    scanf("%d%d",&a,&b);
    int out = sum(a,b);
    printf("Sum of two numbers is %d",out);
}