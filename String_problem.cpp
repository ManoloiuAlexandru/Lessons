/*
Write a C / C ++ program that reads from the keyboard a word of at most 20
characters, only letters of the English alphabet. The program determines the word transformation
read by deleting every small letter of the word, the rest of the letters not changing, as in
example. The program displays the word obtained on the screen. If the word read
contains only lowercase letters, the program will display the message Vid Word.*/

#include <iostream>
#include<cstring>
using namespace std;

int main()
{
    string str;
    char new_string[250];
    int c,hasupperletter=0;
    
    getline (cin, str);
    for(c=0;c<str.length();c++)
        if (str[c]>='A' && str[c]<='Z')
            {hasupperletter=1;
            cout<<str[c];}
    if (hasupperletter==0)
        cout<<"Vid Word";
}
