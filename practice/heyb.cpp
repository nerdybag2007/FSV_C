#include<iostream>
using namespace std;
int main(){
int n,temp,sum=0,r;
cout<<"enter the numbers";
 cin>>n;
 temp=n;
 while (n>0){
    r=n%10;
    sum=sum*10+r;
    n=n/10;
 }
 if(sum==temp){
    cout<<"yes its a palendrome";
 }else{
    cout<<"no its not a palendrome";
 }
 return 0;

}