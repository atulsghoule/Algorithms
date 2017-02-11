//stack using singly linked list
#include<iostream>
using namespace std;
class stack
{
    struct node
    {
        int data;
        node *next;
    };
    node *root;
    int size;
    int current_size;
    public:
    stack(int size)
    {
        root=NULL;
        this->size=size;
        current_size=0;
    }
    void push(int value)
    {
        if(current_size>=size)
        {
            cout<<"Stack Overflow\n";
            return;
        }
        node *new_node=new node();
        new_node->data=value;
        if(root==NULL)
            new_node->next=NULL;
        else
            new_node->next=root;
        root=new_node;
        current_size+=1;
    }
    void pop()
    {
        if(root==NULL)
        {
            cout<<"Stack Underflow\n";
            return;
        }
        node *temp=root;
        root=root->next;
        cout<<temp->data<<" : popped out\n";
        delete temp;
        current_size-=1;
    }
    void print_stack()
    {
        node *temp=root;
        while(temp!=NULL)
        {
            cout<<temp->data<<" ";
            temp=temp->next;
        }
        cout<<endl;
    }
};
