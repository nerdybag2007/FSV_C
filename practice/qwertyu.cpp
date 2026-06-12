#include<iostream>
using namespace std;
class employee{
    private:
int id,salary;
char name[20];
int HRA,TA,DA,TS,AS;
  public:
  void sal(){
    cout<<"enter employee id and name and your salary";
    cin>>id>>name>>salary;

  }
  void hell(){
    HRA=(0.15)*salary;
    TA=(0.1)*salary;
    DA=(0.1)*salary;
    TS=salary+HRA+DA+TA;
    AS=(12)*TS;

  }
  void printer(){
    cout<<"your salary is "<<salary<<"\n your ta is"<<TA<<"\nyour da is"<<DA<<"\nyour ts is"<<TS<<"\nyour as is"<<AS;
  }
};
int main(){
    class employee ob;
    ob.sal();
    ob.hell();
    ob.printer();
    return 0;
}