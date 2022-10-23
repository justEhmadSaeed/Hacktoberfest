#include<iostream>
using namespace std;
void bubble_sort(int arr[],int n)
{
  for(int i=0;i<n-1;i++)
  {
    for(int j=0;j<n-i-1;j++)
    {
      if(arr[j]>arr[j+1])
        swap(arr[j],arr[j+1]);
    }
  }
}
void print(int arr[],int size)
{
  int i;
  for(i=0;i<size;i++)
  {
    cout<<arr[i]<<" ";
  }
  cout<<"\n";
}
int main()
{
  int arr[]={2,20,10,8,3,6,9};
  int n=sizeof(arr)/sizeof(arr[0]);
  cout<<"Array before Sorting"<<endl;
  for(int i=0;i<n;i++)
  {
    cout<<arr[i]<<" ";
  }
  cout<<endl;
  cout<<"Array after Sorting"<<endl;
  bubble_sort(arr,n);
  print(arr,n);
  return 0;


}