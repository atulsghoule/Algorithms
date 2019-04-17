/* selection sort 
    selecting first smallest
    then second smallest.....
*/
#include<iostream>
using namespace std;
void selection_sort(int *array,int size)
{
    int min,location,temp;
    for(int i=0;i<size;i++)
    {
        min=array[i];
        location=i;
        for(int j=i+1;j<size;j++)
        {
            if(array[j]<min)
            {
                location=j;
                min=array[i];
            }
        }
        temp=array[i];
        array[i]=array[location];
        array[location]=temp;
    }
}
int main()
{
    int array[10]={1,3,2,4,5,7,6,8,10,9};
    selection_sort(array,10);
    for(int i=0;i<10;i++)
    {
        cout<<array[i]<<" ";
    }
    cout<<endl;
}