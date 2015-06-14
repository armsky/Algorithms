//
// Created by armsky on 6/14/15.
//

#include "Questions.h"
#include <iostream>
#include <vector>
#include <cstring>
#include <string>

using namespace std;

// Some string examples: http://anaturb.net/C/string_exapm.htm

/*
 * 1. Print all permutations of a string
 */
//vector<string> insertChar(vector<string> result, string sChar){
//    int toRemove = result.size();
//    for (int i=0; i< result.size(); i++){
//        string tString = result[i];
//        for (int j=0; j < tString.size(); j++){
//            result.push_back(tString.insert(tString.begin() + j, sChar));
//        }
//    }
//    result.erase(result.begin(), result.begin() + toRemove);
//    return result;
//}
//
//vector<string> permutation(vector<string> result, string s){
//    if (s.size()-1 > 1)
//        return insertChar(permutation(result, s[s.size()-1]);
//    else
//        return inserChar(permutation(result.push_back(s[0]), s[1]);
//}

/*
 * 1.1 Determine if a string has all unique characters (do not use extra data structure)
 */
bool isUniqueChar(string str){
    if (str.size() > 256)
        return false;
    int set[256] =  {};  // Automatically set to 0s
    for (int i = 0; i < str.size(); ++i){
        int ascii_val = str[i]; // cast char to int, which is a ascii value
        if (set[ascii_val] == 1){
            return false;
        }
        set[ascii_val] = 1;
    }
    return true;
}

/*
 * 1.2 reverse (char* str) which is a null-terminated string.
 */
void reverse(char *str){
    char* end = str;
    char temp;
    if (str){
        while (*end)
            ++end;
        --end;  //Set one char back
    }
    while (str < end){
        temp = *str;
        *str++ = *end;
        *end-- = temp;
    }
}

/*
 * 1.3 Given two strings, decide if one is a permutation of the other
 */
// Sort them and compare.
bool isPermutation(string s1, string s2){
    if (s1.size() != s2.size())
        return false;
    int counts[256] = {};
    for (int i = 0; i < s1.size(); i++){
        int ascii = (int)s1[i];
        counts[ascii]++;
    }
    for (int j = 0; j < s2.size(); j++){
        int ascii = (int)s2[j];
        counts[ascii]--;
        if (counts[ascii] < 0)
            return false;
    }
    return true;
}

/*
 * 1.4 Replace all spaces in a string with '%20'
 */

void replace(string &str){
    for (int i=0; i < str.size(); i++){
        if (str[i] == ' '){ // NOTE: use " " will not work !!!!
            str.erase(i, 1);
            str.insert(i, "%20");
        }
    }
}

/*
 * 1.5 perform basic string compression using the counts of repeated characters.
 * aabcccccaaa => a2b1c5a3
 * But if compressed string smaller than original one, return the original.
 */

string compress(string str){
    string com;
    for (int i,j = 0; i < str.size(); i=j){
        j++;
        while (str[j] == str[i] && j < str.size())
            j++;
        com += str[i]; // append() does not accept char, += accepts string and char
        com.append(to_string(j-i)); // convert int to string use std::to_string(i)
    }
    if (str.size() < com.size())
        return str;
    return com;
}

/*
 * 1.6 Given a NxN matrix, rotate it by 90 degrees.
 */

void rotate(int n, int m[][n]){
    for (int layer = 0; layer < n/2; layer++){
        int start = layer;
        int end = n - 1 - layer;
        for (int i = start; i <= end; i++){
            // 未施工完成！！
            m[start][i] = m[end-i + start][start];
        }
    }
}

/*
 * 1.7 If an element in an MxN matrix is 0, the entire row and column are set to 0
 */
// use two list keep track of col and row that contains 0, and iterate the matrix set to 0

/*
 * 1.8 Use isSubstring only once, decide s2 is a rotation of s1
 */

// Concatenate s2 to s2, test s1 is substring of s2s2.


int main(){
    string s = "abc dsd";
    cout << isUniqueChar(s) << endl;
    char *cstr = new char[s.length() + 1];
    strcpy(cstr, s.c_str());
    reverse(cstr);
    cout << cstr << endl;
    cout << s << endl;
    string sp = "ddbcas";
    cout << isPermutation(s, sp) << endl;
    // 1.4
    replace(s);
    cout << s << endl;
    // 1.5
    string s15 = "aabcccccaaa";
    string cs15 = compress(s15);
    cout << cs15 << endl;

//    vector<string> result;
//    result = permutation(result, s);
//    for (int i=0; i< result.size(); i++)
//        cout << result[i] << " ";
//    cout << endl;
    return 0;
}
