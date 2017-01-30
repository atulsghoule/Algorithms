//insertion sort recursive function
#include<iostream>
using namespace std;
void insertion_sort(int *array,int start,int size)
{
    if(start==(size-1))
        return;
    else
    {
        int key=array[start+1],i=start;
        while(i>-1 and array[i]>key)
        {
            array[i+1]=array[i];
            i-=1;
        }
        array[i+1]=key;
        insertion_sort(array,start+1,size);
    }
}
int main()
{
    int array[10]={10,2,4,3,6,5,7,9,8,1};
    insertion_sort(array,0,10);
    for(int i=0;i<10;i++)
    {
        cout<<array[i]<<" ";    
    }
    cout<<endl;
}