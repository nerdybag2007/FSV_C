#include<iostream>
using namespace std;
int main(){
    int a,temp,r,sum=0,n,greatest;
    cout<<"enter the numbers";
    cin>>n;

 greatest=n%10;
 n/=10;
 cout<<"initial greatrest = "<<greatest<<endl;
 while(n>0){
    r=n%10;
    if(greatest<r){
        greatest=r;
        cout<<"If";
    }
    n=n/10;
    cout<<"r = "<<r<<" n= "<<n<<endl;
}
cout<<"the number which is greatest is"<<greatest;
return 0;
}