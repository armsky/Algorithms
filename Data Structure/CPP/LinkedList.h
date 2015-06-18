//
// Created by armsky on 6/13/15.
//
#include <cstddef>

#ifndef ALGORITHMS_LINKEDLIST_H
#define ALGORITHMS_LINKEDLIST_H

struct Node {
    Node *next;
    int data;
public:
    Node(int d)
            :data(d), next(NULL)
    {}
};

#endif //ALGORITHMS_LINKEDLIST_H
