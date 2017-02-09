#include<iostream>
#include<climits>
using namespace std;
class sorting_foundation
{
    public:
    void merge(int *array,int start,int mid,int end)
    {
        int s1=mid-start+2,s2=end-(mid+1)+2;
        int left[s1],right[s2],i,j,k;
        left[s1-1]=INT_MAX;
        right[s2-1]=INT_MAX;
        for(i=0;i<s1-1;i++)
            left[i]=array[i+start];
        for(i=0;i<s2-1;i++)
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
    void max_heapfy(int *array,int index,int size)
    {
        int left=2*(index+1)-1,right=2*(index+1),maximum=index;
        if(left<=size && array[left]>array[index])
            maximum=left;
        if(right<=size && array[right]>array[maximum])
            maximum=right;
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
};
class sort_made : public sorting_foundation
{
    public:
    void merge_sort(int *array,int start,int end)
    {
        if(start<end)
        {
            int mid=(start+end)/2;
            merge_sort(array,start,mid);
            merge_sort(array,mid+1,end);
            merge(array,start,mid,end);
        }
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
};
int main()
{
    sort_made *a;
    int array[10]={10,9,8,7,6,5,4,3,2,1};
    a->merge_sort(array,0,9);
    for(int i=0;i<10;i++)
        cout<<array[i]<<" ";
    cout<<endl;
    int array_1[10]={10,9,8,7,6,5,4,3,2,1};
    a->heap_sort(array_1,9);
    for(int i=0;i<10;i++)
        cout<<array_1[i]<<" ";
    cout<<endl;
    return 0;
}
