//
// Created by armsky on 6/13/15.
//
#include <cstddef>
#include <iostream>
#include "LinkedList.h"

using namespace std;

Node *head = NULL;

void appendToTail(int d){
    Node *newNode = new Node(d);
    if (head == NULL){
        head = newNode;
        return;
    }
    Node *cur = head;
    while(cur->next){
        cur = cur->next;
    }
    cur->next = newNode;
}

bool deleteNode(int d){
    if (head->data == d) {
        head = head->next;
        return true;
    }
    Node* cur = head;
    while (cur->next != NULL){
        if(cur->next->data == d){
            cur->next = cur->next->next;
            return true;
        }
        cur = cur->next;
    }
    return false;
}

void reverse(Node* cur){
    if (!cur)
        return;
    if (!cur->next){
        head = cur;
        return;
    }
    reverse(cur->next);
    cur->next->next = cur;
    cur->next = NULL;
}

void reverse_iterative(){
    // Need at least three nodes
    if (!head || !head->next)
        return;
    Node *first = head;
    Node *second = head->next;
    Node *third = second->next;
    second->next = first;
    first->next = NULL;

    Node *pre = second;
    Node *cur = third;
    Node *nex;
    while (cur){
        nex = cur->next;
        cur->next = pre;
        pre = cur;
        cur = nex;
    }
    head = pre;
}

void display() {
    Node *list = head;
    while(list) {
        cout << list->data <<" ";
        list = list->next;
    }
    cout << endl;
}

int main(){
    head = new Node(1);
    appendToTail(2);
    appendToTail(3);
    appendToTail(4);
    appendToTail(5);
    appendToTail(6);
    display();
    deleteNode(4);
    display();
    reverse(head);
    display();
    reverse_iterative();
    display();
    return 0;
}
