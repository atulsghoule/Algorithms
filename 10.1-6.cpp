//queue using two stacks
#include<iostream>
using namespace std;
class queue_stack
{
    public:
    void enqueue(int *stack1,int *stack2,int *top1,int *top2,int size,int value)
    {
        if(*top1>=size-1 && *top2>=0)
        {
            cout<<"Queue Overflow\n";
            return;
        }
        else if(*top2<0)
        {
            while(*top1>=0)
            {
                *top2+=1;
                stack2[*top2]=stack1[*top1];
                *top1-=1;
            }
        }
        *top1+=1;
        stack1[*top1]=value;
    }
    void dqueue(int *stack1,int *stack2,int *top1,int *top2,int size)
    {
        if(*top2<0 && *top1<0)
        {
            cout<<"Queue Underflow\n";
            return;
        }
        else if(*top2<0)
        {
            while(*top1>=0)
            {
                *top2+=1;
                stack2[*top2]=stack1[*top1];
                *top1-=1;
            }
        }
        *top2-=1;
    }
};
