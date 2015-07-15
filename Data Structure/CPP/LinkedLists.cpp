//
// Created by armsky on 6/16/15.
//

#include "LinkedLists.h"
#include <iostream>
#include <unordered_map>
#include "LinkedListO.h"

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

/*
 * 2.1 Remove duplicates from unsorted linked lists. (what if do not use temporary buffer)
 */
// 1) use hashtable, O(1) time, O(n) space
// In C++, unordered_map is hashtable, O(1) access; map is hashmap, O(log n) access
void removeDup(Node *head){
    unordered_map<int, bool> values;
    Node *pre = head;
    Node *cur = head->next;
    values[head->data] = true;

    while(cur){
        cout << values[cur->data] << endl;
        // find() will return a iterator
        if (values.find(cur->data)->second == false){
            values[cur->data] = true;
            pre = cur;
        }else{
            pre->next = cur->next;
        }
        cur = cur->next;
    }
}
// 2) If not using extra data structure, do runner pointers, O(1) space but O(n^2) time.
void removeDup2(Node *head){
    Node *runner;
    Node *cur = head;
    while (cur){
        runner = cur;
        while (runner->next){
            if (runner->next->data == cur->data){
                runner->next = runner->next->next;
            }else{
                runner = runner->next;
            }

        }
        cur = cur->next;
        cout << cur->data << endl;
        head->display();
    }
}

/*
 * 2.2 Find kth to last element of a singly linked list.
 */
// 1). Recursively
Node* findK(Node *head, int k, int &i){
    if (!head)
        return NULL;
    Node* node = findK(head->next, k, i);
    i++;
    if (i == k)
        return head;
    return node;
}
// 2). use two pointers, with k nodes apart

/*
 * 2.3 delete a node in the middle of a singly linked list.
 * Given only access to that node, no access to head.
 */
bool deleteMid(Node* node){
    if (!node || !node->next)
        return false;
    Node *nex = node->next;
    node->data = nex->data;
    node->next = nex->next;
    return true;
}

/*
 * 2.4 Partition a linked list around a value x, all nodes less than x before all nodes >= x.
 */
// Create two new lists and merge them

/*
 * 2.5 Sum of two linked lists.
 * Input: (7->1->6)+(5->9->2) that is 617+295
 * Output: 2->1->9 that is 912
 */
Node* linkSum(Node *head1, Node *head2){
    int carry = 0;
    Node* newNode;
    Node* dummy;
    dummy->next = newNode;
    while (head1 && head2) {
        int sum = head1->data + head2->data + carry;
        newNode->data = sum;
        carry = 0;
        if (sum >= 10) {
            sum = sum % 10;
            carry = 1;
        }
        head1 = head1->next;
        head2 = head2->next;
        if (head1 || head2) {
            newNode->next = new Node(0);
            newNode = newNode->next;
        }
    }
    if (head1)
        newNode->next = head1;
    if (head2)
        newNode->next = head2;
    return dummy->next;
}

int main(){
    Node *head = new Node(1);
    head->appendToTail(2);
    head->appendToTail(3);
    head->appendToTail(2);
    head->appendToTail(5);
    head->appendToTail(3);
    head->display();
    Node *head2 = new Node(7);
    head2->appendToTail(8);
    head2->appendToTail(9);
    head2->display();
    // 2.1
//    removeDup2(head);
//    head->display();
    // 2.2
//    Node* node = findK(head, 2, 0);
//    cout << node->data;
    // 2.3
//    cout << deleteMid(head->next->next);
//    head->display();
    // 2.4
    Node* head3 = linkSum(head, head2);
    head3->display();

    return 0;
}
