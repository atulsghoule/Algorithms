#include<iostream>
using namespace std;
void max_heapfy(int *array,int index,int size)
{
    int l_ch=2*(index+1)-1,r_ch=2*(index),maximum=index;
    if(l_ch<=size && array[l_ch]>array[index])
        maximum=l_ch;
    if(r_ch<=size && array[r_ch]>array[maximum])
        maximum=r_ch;
    if(maximum!=index)
    {
        array[maximum]=array[index]^array[maximum];
        array[index]=array[index]^array[maximum];
        array[maximum]=array[index]^array[maximum];
        max_heapfy(array,maximum,size);
    }
}
void build_max_heap(int *array,int size)
{
    for(int i=size/2;i>-1;i--)
        max_heapfy(array,i,size);
}
void heap_sort(int *array,int size)
{
    build_max_heap(array,size);
    for(int i=0;i<size;i++)
    {
        array[size-i]=array[0]^array[size-i];
        array[0]=array[0]^array[size-i];
        array[size-i]=array[0]^array[size-i];
        max_heapfy(array,0,size-i-1);
    }
}
int main()
{
    int array[10]={10,9,8,7,6,5,4,3,2,1};
    heap_sort(array,9);
    for(int i=0;i<10;i++)
        cout<<array[i]<<" ";
    cout<<endl;
}
