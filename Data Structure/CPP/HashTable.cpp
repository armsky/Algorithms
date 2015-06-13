//
// Created by armsky on 6/12/15.
//

#include "HashTable.h"

class HashEntry{
private:
    int key;
    int value;

public:
    HashEntry(int key, int value){
        this->key = key;
        this->value = value;
    }

    int getKey(){
        return this->key;
    }

    int getValue(){
        return this->value;
    }
};

const int TABLE_SIZE = 128;

class HashTable{

};
