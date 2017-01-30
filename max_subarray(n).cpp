#include<iostream>
#include<climits>
using namespace std;
int main()
{
    int array[7]={1,2,3,-7,1,1,7};
    int max_temp=array[0],max_ans=array[0],size=7;
    for(int i=1;i<size;i++)
    {
        max_temp=max(array[i],max_temp+array[i]);
        max_ans=max(max_temp,max_ans);
    }
    cout<<max_ans<<endl;
    return 0;
}