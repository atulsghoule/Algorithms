//two stack in one array
#include<iostream>
using namespace std;
class stack_two
{
    public:
    void push_stack_1(int *array,int *top_stack_1,int *top_stack_2,int size,int value)
    {
        if(*top_stack_1+1+(size-*top_stack_2+1)>=size || *top_stack_1+1>=*top_stack_2)
            cout<<"Stack Overflow\n";
        else
        {
            *top_stack_1+=1;
            array[*top_stack_1]=value;
        }
    }
    void pop_stack_1(int *array,int *top_stack_1)
    {
        if(*top_stack_1<0)
            cout<<"Stack Underflow\n";
        else
            *top_stack_1-=1;
    }
    void push_stack_2(int *array,int *top_stack_1,int *top_stack_2,int size,int value)
    {
        if(*top_stack_1+1+(size-*top_stack_2+1)>=size || *top_stack_2-1<=*top_stack_1)
            cout<<"Stack Overflow\n";
        else
        {
            *top_stack_2-=1;
            array[*top_stack_2]=value;
        }
    }
    void pop_stack_2(int *array,int *top_stack_2,int size)
    {
        if(*top_stack_2>size-1)
            cout<<"Stack Underflow\n";
        else
            *top_stack_2-=1;
    }
};
