#include <stdio.h>
struct employee
{
    int id, salary;
    char name[30];
    int HRA,TA,DA,TS,AS;
};
void main()
{
    int n, i;
    printf("neter the nummber of employyeeeesssss");
    scanf("%d", &n);
    struct employee e[n];
    for (i=0;i<n;i++){
          printf("Enter employee id %d\t", i+1);
        scanf("%d",&e[i].id);

        printf("Enter name\t");
        scanf("%s",&e[i].name);
        
        printf("Enter salary\t");
        scanf("%d",&e[i].salary);
        
        e[i].HRA=(0.15)*e[i].salary;
        e[i].TA=(0.01)*e[i].salary;
        e[i].DA=(0.01)*e[i].salary;
        
        e[i].TS=e[i].salary+e[i].HRA+e[i].TA+e[i].DA;
        e[i].AS=(12*e[i].TS);

    }
    for (i=0;i<n;i++){
     printf("\n>>>>>>Employee DATA\n");
        printf("Empoyee ID ==== %d\n",e[i].id);
        printf("Empoyee NAME ==== %s\n",e[i].name);
        printf("Empoyee SALARY ==== %d\n",e[i].salary);
        printf("your hra is %d\n",e[i].HRA);
        printf("your TA is %d\n",e[i].TA);
        printf("your da is %d\n",e[i].DA);
        printf("your TS is  %d\n",e[i].TS);
        printf("your AS is  %d\n",e[i].AS);
    }
    

}