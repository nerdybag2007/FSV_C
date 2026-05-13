#include<stdio.h>
void main(){
    int arr[5];
    int i,j;
    int arr1[5];
    int arr2[5];
    int sum;
    for(i=0;i<5;i++){
        printf("enter a number %d of array 1",i);
        scanf("%d",&arr1[i]);
    }
    for(i=0;i<5;i++){
        printf("enter a number %d of array 2",i);
        scanf("%d",&arr2[i]);
    }
    for(i=0;i<5;i++){
        // arr[i]=0;
    arr[i]=arr1[i]+arr2[i];
    }
   for(i=0;i<5;i++){
       
       printf("%d ",arr[i]);
    }

}