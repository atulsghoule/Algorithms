#include<iostream>
#include<climits>
using namespace std;
int temp[3];
int *max_subarray(int *array,int low,int high);
int *max_crossing(int *array,int low,int mid,int high);
int main()
{
    int array[7]={2,3,4,-2,5,6,-3};
    int *ans;
    ans=max_subarray(array,0,6);
    cout<<ans[0]<<" "<<ans[1]<<" "<<ans[2]<<endl;
    return 0;
}
int *max_subarray(int *array,int low,int high)
{
     if(low==high)
    {
        static int ans[3]={array[low],low,high};
        return ans;   
    }
    else
    {
        static int *left,*right,*cross;
        int mid=(low+high)/2;
        left=max_subarray(array,low,mid);
        right=max_subarray(array,mid+1,high);
        cross=max_crossing(array,low,mid,high);
        if(left[0]>right[0]&&left[0]>cross[0])
            return left;
        else if(right[0]>cross[0])
            return right;
        else
            return cross;
    }
}
int *max_crossing(int *array,int low,int mid,int high)
{
    int left_sum=INT_MIN,sum=0,i,max_left,max_right;
    for(i=mid;i>low-1;i--)
    {
        sum+=array[i];
        if(sum>left_sum)
        {
            left_sum=sum;
            max_left=i;
        }
    }
    int right_sum=INT_MIN;
    sum=0;
    for(i=mid+1;i<high+1;i++)
    {
        sum+=array[i];
        if(sum>right_sum)
        {
            right_sum=sum;
            max_right=i;
        }
    }
    temp[0]=right_sum+left_sum;
    temp[1]=max_left;
    temp[2]=max_right;
    return temp;
}