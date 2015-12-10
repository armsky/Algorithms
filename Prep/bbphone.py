// This is the text editor interface.
// Anything you type or change here will be seen by the other person in real time.

import java.util.*;

public class HelloWorld {

    public static boolean isSentence(String s, HashSet<String> d) {
        return false;
    }


    public static void main(String[] args) {
        // Prints "Hello, World" to the terminal window.
        HashSet<String> dictionary=new HashSet<String> ();
        dictionary.add("I");
        dictionary.add("LOVE");
        dictionary.add("TO");
        dictionary.add("EAT");
        dictionary.add("TACOS");
        dictionary.add("MEET");
        dictionary.add("ME");
        dictionary.add("THERE");

        String s="ILOVETOEATTACOS";
        //String s="MEETMETHERE";


        System.out.println(isSentence(s,dictionary));
    }

}

def isSentence(s, d):
    if not s:
        return True
    if s in d:
        return True
    mark = False
    for i in range(1, len(s)+1):
        if s[0:i] in d:
            if isSentence(s[i:], d):
                mark = True
    return mark

s = "AILOVE"
print isSentence(s,d)
s = "ILOVE"
print isSentence(s,d)
s = "ILOVEA"
print isSentence(s,d)
s="ILOVETOEATTACOS"
print isSentence(s,d)
s="MEETMETHERE"
print isSentence(s,d)
