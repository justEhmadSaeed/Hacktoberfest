#include<iostream>
using namespace std;
int main()
{
    int row;
    cout<<"enter rows for butterfly"<<endl;
        cin>>row;
    for(int i=1;i<=row;i++)
    {    for(int j=1;j<=2*row;j++)
        {
            if(i>=j || j>(2*row-i))
                cout<<"* ";
            else cout<<"  ";
        }
        cout<<endl;
    }
    for(int i=row;i>0;i--)
    {    for(int j=1;j<=2*row;j++)
        {
            if(i>=j || j>(2*row-i))
                cout<<"* ";
            else cout<<"  ";
        }
        cout<<endl;
    }
 return 0;   
}
