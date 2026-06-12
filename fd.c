#include <stdio.h>
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
    return 0;
}