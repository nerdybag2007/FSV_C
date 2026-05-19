#include <stdio.h>
struct student
{
    int rollno;
    char name[20];
    int arr[5];
    int total, percentage, average;
};
void main()
{
    int n;
    struct student s1;
    int i;
    printf("enter roll no");
    scanf("%d", &s1.rollno);
    printf("enter name");
    scanf("%s", &s1.name);
    printf("my name is %s \nroll no is nigga %d", s1.name, s1.rollno);
    s1.total = 0;
    for (i = 0; i <= 4; i++)
    {
        printf("enter the number");
        scanf("%d", &s1.arr[i]);
        s1.total = s1.total + s1.arr[i];
    }
    s1.percentage = (s1.total * 100) / 500;
    s1.average = s1.total / 5;
    printf("your percentage is %d and total is %d and average is %d", s1.percentage, s1.total, s1.average);
    if (s1.percentage >= 90 && s1.percentage <= 100)

    {
        printf("your grade is A");
    }
    else if (s1.percentage >= 80 && s1.percentage <= 90)
    {
        printf("your grade is B you did the best bro the best ");
    }
    else if (s1.percentage >= 70 && s1.percentage <= 80)
    {
        printf("your grade is c bro you did good just some more next time?");
    }
    else if (s1.percentage <= 60)
    {
        printf("your grade is d ");
    }
}
