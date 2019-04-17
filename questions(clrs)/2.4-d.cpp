#include<iostream>
#include<climits>
using namespace std;
int ans=0,maxint=INT_MAX;
void custom_merge(int *array,int start,int mid,int end);
void custom_merge_sort(int *array,int start,int end);
int main()
{
    int array[6]={8,2,4,4,3,1},size=6;
    custom_merge_sort(array,0,size-1);
    cout<<ans<<endl;
    for(int i=0;i<size;i++) 
        cout<<array[i]<<" ";
    cout<<endl;
    return 0;
}
void custom_merge_sort(int *array,int start,int end)
{
    if(end>start)
    {
        int mid=(end+start)/2;
        custom_merge_sort(array,start,mid);
        custom_merge_sort(array,mid+1,end);
        custom_merge(array,start,mid,end);
    }
}
void custom_merge(int *array,int start,int mid,int end)
{
    int s1=mid-start+2,s2=end-mid+1;
    int left[s1],right[s2],i,j,k;
    left[s1-1]=maxint;
    right[s2-1]=maxint;
    for(i=start;i<mid+1;i++)
        left[i-start]=array[i];
    for(i=mid+1;i<end+1;i++)
        right[i-(mid+1)]=array[i];
    i=0;
    j=0;
    for(k=start;k<end+1;k++)
    {
        if(left[i]>right[j])
        {
            if(left[i]!=maxint)
                ans+=(s1-k+j-1+start);
            array[k]=right[j];
            j+=1;
        }
        else
        {
            array[k]=left[i];
            i+=1;
        }
    }
}