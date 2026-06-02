#include<stdio.h>
int main() {
    float A, B, C, D, E;
    float sum, average, percentage;
 printf("Enter marks for 5 subjects: ");
    scanf("%f %f %f %f %f", &A, &B, &C, &D, &E);
sum = A + B + C + D + E;
average = sum / 5;
percentage = (sum / 500) * 100;
    printf("sum: %f", sum);
    printf("Average: %f", average);
    printf("Percentage: %f", percentage);
    if(percentage>=90){
        printf("congratulations your grade is a");

    }else if((percentage>70)&&(percentage<90)){
        printf("your grade is b need improvement");
    }
    else if(( percentage>33)&&(percentage<=70))
    {printf("your grade is c try hard lil nigga");

    }
    else if((percentage>=0)&&(percentage<=33))
    {
        printf("teri to feilding set hai bro");
    }

}