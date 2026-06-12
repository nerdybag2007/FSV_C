#include<iostream>
// using namespace std;
void loop(int n){
    if(n>0){
        std::cout<<"hi ";
        loop(n-1);  
    }
}
int main(){
    int n;
    std::cout<<"Enter n";
    std::cin>>n;
    loop(n);
 return 0;
}