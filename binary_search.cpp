#include<iostream>
using namespace std;
bool search(int *array,int start,int end,int num)
{
    if(end>=start)
    {
        int mid=start+(end-start)/2;
        if(array[mid]==num)
            return true;
        else if(array[mid]>num)
            return search(array,start,mid-1,num);
        return search(array,mid+1,end,num);
    }
    return false;
}
int main()
{
    int num,array[10]={1,2,3,4,5,6,7,8,9,10};
    cin>>num;
    if(search(array,0,9,num))
        cout<<"true\n";
    else
        cout<<"false\n";
    return 0;
    //
}