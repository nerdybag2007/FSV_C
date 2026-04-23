#include<stdio.h>
int main() {
    float A, B, C, D, E;
    float total, average, percentage;
 printf("Enter marks for 5 subjects: ");
    scanf("%f %f %f %f %f", &A, &B, &C, &D, &E);
total = A + B + C + D + E;
average = total / 5;
percentage = (total / 500) * 100;
    printf("Total: %f", total);
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