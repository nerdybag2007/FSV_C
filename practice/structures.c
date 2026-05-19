#include <stdio.h>
struct student
{
    int rollno;
    char name[20];
    int marks[5];
    int total, percentage, average;
};
void main()
{
    //VARIABLES
    int n, i,j;

    //USER COUNT INPUT
    printf("enter number of jailers");
    scanf("%d", &n);

    //STRUCTURE INSTANCE
    struct student e[n];

    //MAIN LOOP
    for (i = 0; i < n; i++)
    {
        printf("Enter rollno \t");
        scanf("%d", &e[i].rollno);

        printf("Enter name\t");
        scanf("%s", &e[i].name);

        e[i].total = 0;
        for (j = 0; j < 5; j++)
        {
            printf("Subject %d marks",j+1);
            scanf("%d", &e[i].marks[j]);
            e[i].total = e[i].total + e[i].marks[j];
        }
        e[i].percentage = (e[i].total * 100) / 500;
        e[i].average = e[i].total / 5;
    }
    
    //PRINTING LOOP
    for(i=0;i<n;i++){
        
        printf("\nmy name is %s \nroll no is nigga %d", e[i].name, e[i].rollno);
        printf("\nyour percentage is %d \ntotal is %d \naverage is %d", e[i].percentage, e[i].total, e[i].average);
        if (e[i].percentage >= 90 && e[i].percentage <= 100)
        {
            printf("\nyour grade is A");
        }
        else if (e[i].percentage >= 80 && e[i].percentage < 90)
        {
            printf("\nyour grade is B you did the best bro the best ");
        }
        else if (e[i].percentage >= 60 && e[i].percentage < 80)
        {
            printf("\nyour grade is c bro you did good just some more next time?");
        }
        else if (e[i].percentage < 60)
        {
            printf("\nyour grade is d ");
        }
    }
}
