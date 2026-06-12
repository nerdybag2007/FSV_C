#include<stdio.h>
int main(){
    int arr[5];
    int i;
    int sum;
    float sum=0, average, percentage;
  for(i=0;i<5;i++){
    printf("enter users marks:");
    scanf("%d",&arr[i]);
    sum=sum+arr[i];
  }
    average=sum/5;
    percentage=(sum*100)/500;
  
printf("the sum,average and percentage of users are are %f,%f,%f",sum,average,percentage);
 if(percentage>=90){
        printf("bitch ass bullshit");

    }else if((percentage>70)&&(percentage<90)){
        printf("");
    }
    else if(( percentage>33)&&(percentage<=70))
    {printf("wassup my n word");

    }
    else if((percentage>=0)&&(percentage<=33))
    {
        printf("you forget a thousand things a day pal make sure this is one of em -micheal de santa");
    }

}