//
// Created by armsky on 6/16/15.
//

#include "LinkedListO.h"
#include <iostream>
#include <cstddef>

using namespace std;

/* definition of the list node class */
Node::Node(int d){
    this->data = d;
    this->next = NULL;
}

void Node::appendToTail(int d){
    Node *newNode = new Node(d);
    Node *cur = this;
    while (cur->next){
        cur = cur->next;
    }
    cur->next = newNode;
}

Node Node::deleteNode(int d){
    if (this->data == d){
        return *this->next;
    }
    Node *cur = this;
    while (cur->next != NULL){
        if (cur->next->data == d){
            cur->next = cur->next->next;
            return *this;
        }
        cur = cur->next;
    }
    return *this;
}

void Node::display(){
    Node *list = this;
    while (list){
        cout << list->data <<" ";
        list = list->next;
    }
    cout << endl;
}


int main(){
    Node head = Node(1);
    head.appendToTail(2);
    head.appendToTail(3);
    head.appendToTail(4);
    head.appendToTail(5);
    head.appendToTail(6);
    head.display();
    head = head.deleteNode(1);
    head.display();
    return 0;
}
