#include<iostream>
using namespace std;
int main(){
    int a,temp,r,sum=0,n,e=0,o=0;
    cout<<"enter the numbers";
 cin>>n;
 temp=n;
 while(n>0){r=n%10;
    if(r%2==0){
        e++;
    }
    else{
        o++;
    }
    n=n/10;
}
cout<<"even numbers are "<<e <<endl;
cout<<"odd numbers are  "<<o <<endl;

return 0;
}