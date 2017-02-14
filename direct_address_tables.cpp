//direct address table
//room => person
#include<iostream>
#include<string>
using namespace std;
class direct_address
{
    struct person
    {
        string name;
    };
    struct room
    {
        person* next;
    };
    public:
    int size;
    room *rooms;
    direct_address(int size)
    {
        this->size=size;
        rooms = new room [size];
        for(int i=0;i<size;i++)
            rooms[i].next=NULL;
    }
    void insert_value(int room_num,string value)
    {
        person *new_person=new person;
        rooms[room_num-1].next=new_person;
        new_person->name=value;
    }
    void delete_value(int room_num)
    {
        delete rooms[room_num-1].next;
        rooms[room_num-1].next=NULL;
    }
    void search_value(int room_num)
    {
        if(rooms[room_num-1].next==NULL)
            cout<<"Room No. : "<<room_num<<" Vacant\n";
        else 
            cout<<"Room No. : "<<room_num<<" "<<rooms[room_num-1].next->name<<"\n";
    }
    void display()
    {
        for(int i=0;i<size;i++)
        {
            if(rooms[i].next==NULL)
                cout<<"Room No. : "<<i+1<<" Vacant\n";
            else 
                cout<<"Room No. : "<<i+1<<" "<<rooms[i].next->name<<"\n";  
        }
    }
    ~direct_address()
    {
        for(int i=0;i<size;i++)
        {
            if(rooms[i].next!=NULL)
                delete rooms[i].next;
        }
        delete [] rooms;
    }
};

int main()
{
    direct_address *table=new direct_address(5);
    table->insert_value(1,"A");
    table->insert_value(2,"B");
    table->insert_value(3,"C");
    table->insert_value(4,"D");
    table->insert_value(5,"E");
    table->search_value(3);
    delete table;
}