#include<stdio.h>
int main(){
  float A,B,C,D,E;
  float sum, average, percentage;
    printf("enter users marks:");
    scanf("%f%f%f%f%f",&A,&B,&C,&D,&E);
    sum=A+B+C+D+E;
    average=sum/5;
    percentage=(sum*100)/500;
  
printf("the sum,average and percentage of users are are %f,%f,%f",sum,average,percentage);

}