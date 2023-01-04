#include <iostream>
using namespace std;
int main()
{
int num,num2,i;
string str;
cin >> num >> num2 >> str;
if( num == num2){
cout << "Numbers_are_equal" << endl;
}
for(i=0; i<num; i++ ){
cout << str << endl;
}
return 0;
}