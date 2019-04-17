//quick_sort ..
#include<iostream>
using namespace std;
void quick_sort(int *array,int start,int end);
int partition(int *array,int start,int end);
int main()
{
    int array[10]={10,9,8,7,6,5,3,4,1,2};
    quick_sort(array,0,9);
    for(int i=0;i<10;i++)
        cout<<array[i]<<" ";
    cout<<endl;
    return 0;
}
void quick_sort(int *array,int start,int end)
{
    if(start<end)
    {
        int pi=partition(array,start,end);
        quick_sort(array,start,pi-1);
        quick_sort(array,pi+1,end);
    }
}
int partition(int *array,int start,int end)
{
    int element=array[end];
    int wall=start-1,temp;
    for(int j=start;j<end;j++)
    {
        if(array[j]<=element)
        {
            wall+=1;
            temp=array[j];
            array[j]=array[wall];
            array[wall]=temp;
        }
    }
    temp=array[wall+1];
    array[wall+1]=array[end];
    array[end]=temp;
    return wall+1;
}