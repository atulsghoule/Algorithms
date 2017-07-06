#include<iostream>
#include<stack>
using namespace std;
struct node{
    int data;
    node* l_child;
    node* r_child;
};
node* insert(node *root,int num){
    if(root==NULL){
        node *new_node=new node;
        new_node->data=num;
        new_node->l_child=NULL;
        new_node->r_child=NULL;
        root=new_node;
    }
    else if(root->data>num)
        root->l_child=insert(root->l_child,num);
    else
        root->r_child=insert(root->r_child,num);
    return root;
}
int main(){
    node *root=NULL;
    root=insert(root,5);
    root=insert(root,3);
    root=insert(root,4);
    root=insert(root,8);
    root=insert(root,1);
    stack<node*> a;
    node* current=root;
    bool done=true;
    while(done){
        if(current!=NULL){
            a.push(current);
            current=current->l_child;
        }
        else{
            if(a.size()!=0){
                current=a.top();
                a.pop();
                cout<<current->data<<" ";
                current=current->r_child;
            }
            else
                done=!done;
        }
        
    }
    return 0;
}