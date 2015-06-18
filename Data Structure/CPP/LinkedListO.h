//
// Created by armsky on 6/16/15.
//

#ifndef ALGORITHMS_LINKEDLISTO_H
#define ALGORITHMS_LINKEDLISTO_H


class Node {
public:
    Node *next;
    int data;
public:
    Node(int d);
    void appendToTail(int);
    Node deleteNode(int);
    void display();
};


#endif //ALGORITHMS_LINKEDLISTO_H
