/*
    Insertion sort
    start with second position and put into right place on the left
    eg sorting cards
*/
#include<iostream>
using namespace std;
void insertion_sort(int *array,int size)
{
    int j=0,key;
    for(int i=1;i<size;i++)
    {
        key=array[i];
        j=i-1;
        while(j>-1 && array[j]>key)
        {
            array[j+1]=array[j];
            j-=1;
        }
        array[j+1]=key;
    }
}
int main()
{
    int array[10]={1,2,3,5,6,4,9,8,7,10};
    insertion_sort(array,10);
    for(int i=0;i<10;i++)
    {
        cout<<array[i]<<" ";
    }
    cout<<endl;
}
