//queue using linked list
#include<iostream>
using namespace std;
class queue
{
    struct node
    {
        int data;
        node *next;
    };
    node *end;
    node *front;
    int size;
    int current_size;
    public:
    queue(int size)
    {
        this->size=size;
        front=NULL;
        end=NULL;
        current_size=0;
    }
    void enqueue(int value)
    {
        if(current_size>=size)
        {
            cout<<"Queue Overflow\n";
            return ;
        }
        node *new_node=new node();
        new_node->data=value;
        if(front==NULL)
            front=new_node;
        if(end!=NULL)
            end->next=new_node;
        end=new_node;
        new_node->next=NULL;
        current_size+=1;
    }
    void dequeu()
    {
        if(current_size<=0)
        {
            cout<<"Queue Underflow\n";
            return;
        }
        node *temp=front;
        if(end==front)
            end=NULL;
        front=front->next;
        cout<<temp->data<<" : dequed \n";
        delete temp;
        current_size-=1;
    }
    void print()
    {
        node *temp=front;
        while(temp!=NULL)
        {
            cout<<temp->data<<" ";
            temp=temp->next;
        }
        cout<<endl;
    }
};
