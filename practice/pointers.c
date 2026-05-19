#include <stdio.h>
struct student
{
    int rollno;
    char name[20];
};
void main()
{
    struct student s1;
    struct student *s2;
    printf("enter roll no");
    scanf("%d", &s1.rollno);
    printf("enter name");
    scanf("%s", &s1.name);
    s2 = &s1;
    printf("my name is %s and rollno is %d", s2->name, s2->rollno);
}