#include<stdio.h>
int main(){
    int arr[5];
    int i;
    int sum;
    float total=0, average, percentage;
  for(i=0;i<5;i++){
    printf("enter users marks:");
    scanf("%d",&arr[i]);
    total=total+arr[i];
  }
    average=total/5;
    percentage=(total*100)/500;
  
printf("the total,average and percentage of users are are %f,%f,%f",total,average,percentage);
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