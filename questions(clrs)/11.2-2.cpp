#include<iostream>
using namespace std;
class hash_1
{
    struct node
    {
        int data;
        node *next;
        node *pre;
    };
    int size;
    node *table[9];
    public:
    hash_1()
    {
        size=9;
        for(int i=0;i<size;i++)
            table[i]=NULL;
    }
    int hash_func(int num)
    {
        return num%9;
    }
    void insert(int num)
    {
        int pos=hash_func(num);
        node *new_node=new node;
        new_node->data=num;
        new_node->next=table[pos];
        if(table[pos]!=NULL)
            table[pos]->pre=new_node;
        table[pos]=new_node;
    }
    void display()
    {
        node *temp;
        for(int i=0;i<size;i++)
        {
            temp=table[i];
            while(temp!=NULL)
            {
                cout<<temp->data<<" ";
                temp=temp->next;
            }
            cout<<"\n";
        }
    }
    ~hash_1()
    {
        node *temp;
        for(int i=0;i<size;i++)
        {
            temp=table[i]->next;
            while(temp!=NULL)
            {
                temp=temp->next;
                delete temp;
            }
            delete temp;
        }
    }
};
int main()
{
    hash_1 *table=new hash_1();
    table->insert(5);
    table->insert(28);
    table->insert(19);
    table->insert(15);
    table->insert(20);
    table->insert(33);
    table->insert(12);
    table->insert(17);
    table->insert(10);
    table->display();
    delete table;
}