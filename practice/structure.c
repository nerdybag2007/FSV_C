#include<stdio.h>

struct employee{
    int id,salary;
    char name[30];
};

void main(){
    int n,i;
    printf("enter no of employee");
    scanf("%d",&n);

    struct employee e[n];

    for(i=0 ; i<n ; i++){
        printf("Enter employee id %d\t", i+1);
        scanf("%d",&e[i].id);

        printf("Enter name\t");
        scanf("%s",&e[i].name);

        printf("Enter salary\t");
        scanf("%d",&e[i].salary);
    }

    for(i=0;i<n;i++){
        printf("\n>>>>>>Employee DATA\n");
        printf("Empoyee ID ==== %d\n",e[i].id);
        printf("Empoyee NAME ==== %s\n",e[i].name);
        printf("Empoyee SALARY ==== %d\n",e[i].salary);
    }
}