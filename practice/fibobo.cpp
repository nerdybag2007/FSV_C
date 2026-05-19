#include<iostream>
using namespace std;
int main(){
    int i,n,a=0,b=1,sum;
    cout<<"enter the number of terms";
cin>>n;
cout<<a<<" "<<b <<" ";
for(i=1;i<=n;i++){
    sum=a+b;
    a=b;
    cout<<sum" ";
    b=sum;
}
}
