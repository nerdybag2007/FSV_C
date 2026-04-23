#include<stdio.h>
int main(){
  float A,B,C,D,E;
  float total, average, percentage;
    printf("enter users marks:");
    scanf("%f%f%f%f%f",&A,&B,&C,&D,&E);
    total=A+B+C+D+E;
    average=total/5;
    percentage=(total*100)/500;
  
printf("the total,average and percentage of users are are %f,%f,%f",total,average,percentage);

}