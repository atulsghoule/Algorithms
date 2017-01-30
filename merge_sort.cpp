/*
    merge sort divide and concure
    stratergy
*/
#include<iostream>
#include<climits>
using namespace std;
//merge_sort parameter start and end indecies
void merge(int*,int ,int ,int );
void merge_sort(int *,int ,int );
int main()
{
    int array[10]={10,8,7,9,4,5,6,2,3,1};
    merge_sort(array,0,9);
    for(int i=0;i<10;i++)
    {
        cout<<array[i]<<" "; 
    }
    cout<<endl;
    return 0;
}
void merge_sort(int * array,int start ,int end)
{
    int mid;
    if(start<end)
    {
        mid=(end+start)/2;
        merge_sort(array,start,mid);
        merge_sort(array,mid+1,end);
        merge(array,start,mid,end);
    }
}
void merge(int *array,int start,int mid,int end)
{
    int s1=(mid-start)+1,s2=(end-mid),i,j,k;
    int left[s1+1],right[s2+1];
    left[s1]=INT_MAX;
    right[s2]=INT_MAX;
    for(i=0;i<s1;i++)
        left[i]=array[i+start];
    for(i=0;i<s2;i++)
        right[i]=array[i+mid+1];
    i=0;
    j=0;
    for(k=start;k<end+1;k++)
    {
        if(left[i]<right[j])
        {
           array[k]=left[i];
           i+=1;
        }
        else
        {
            array[k]=right[j];
            j+=1;
        }
    }
}