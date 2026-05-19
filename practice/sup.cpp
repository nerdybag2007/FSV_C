#include<iostream>
using namespace std;
int main(){
    int a,b,c,d;
cout<<"enter the numbers";
    cin>>a>>b>>c>>d;
    (a>b&&a>c&&a>d)?cout<<"a is greatest":(b>c&&b>d)? cout<<"b is greatest":(c>d)?cout<<"c is greatest":cout<<"d is greatest";
    return 0;
}