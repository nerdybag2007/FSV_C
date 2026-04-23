#include <stdio.h>
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
    return 0;
}