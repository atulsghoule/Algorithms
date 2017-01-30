#include<iostream>
using namespace std;
int  binary_search(int *array,int start,int end,int num)
{
    if(start<=end)
    {
        int mid=start+(end-start)/2;
        if(array[mid]==num)
            return num;
        if(array[mid]>num)
            return binary_search(array,start,mid-1,num);
        return binary_search(array,mid+1,end,num);
    }
    return -1;
}
int main()
{
    // sorted O(n*lg(n))
    int k,array[10]={1,2,3,4,5,6,7,8,9,10};
    cin>>k;
    int num1=-1,num2=-1,temp;
    //complexity O(n*log(n))
    for(int i=0;i<10;i++)
    {
        temp=binary_search(array,i+1,10,k-array[i]);
        if(temp!=-1)
        {
            num1=array[i];
            num2=temp;
            break;
        }
    }
    if(num1!=-1)
        cout<<num1<<" "<<num2<<endl; 
    else
        cout<<"no such pair\n";
}
