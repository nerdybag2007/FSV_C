#include<stdio.h>
void mai(){
    int arr[5]={5,7,2,1,8};
    int key;
    int i;
    printf("enter a number ");
    scanf("%d",&key);
    for(i=0;i<5;i++){
        if(key==arr[i]){
            printf("%d",i);


        }else{
            printf("-1");
        }
    }
    

}