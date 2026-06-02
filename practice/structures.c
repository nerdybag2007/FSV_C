#include <stdio.h>
struct student
{
    int rollno;
    char name[20];
    int marks[5];
    int sum, percentage, average;
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

        e[i].sum = 0;
        for (j = 0; j < 5; j++)
        {
            printf("Subject %d marks",j+1);
            scanf("%d", &e[i].marks[j]);
            e[i].sum = e[i].sum + e[i].marks[j];
        }
        e[i].percentage = (e[i].sum * 100) / 500;
        e[i].average = e[i].sum / 5;
    }
    
    //PRINTING LOOP
    for(i=0;i<n;i++){
        
        printf("\nmy name is %s \nroll no is nigga %d", e[i].name, e[i].rollno);
        printf("\nyour percentage is %d \nsum is %d \naverage is %d", e[i].percentage, e[i].sum, e[i].average);
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
