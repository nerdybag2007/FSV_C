#include<stdio.h>
#include<string.h>
void main(){
    char name[20];
    char name2[20];
    // printf("Enter name");
    // puts("Enter name");
    printf("enter your name");
    scanf("%s",&name);
    

    int num = strlen(name);
    
    strlwr(name); 
    strup(name); //STRING TO UPPER CASE;
    strcpy(name2,name);
    printf("my name is %s",name);
    
}
