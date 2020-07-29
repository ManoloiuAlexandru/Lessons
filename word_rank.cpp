/*
Write a program that gets from input a sentence, counts word frequencies, and prints one line for each word and frequencies
*/
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iterator>
#include <map>
using namespace std;
void count_word(string word, vector<string> words_in_text,map<string,int> &word_rank)
{
    int nr_of_app = 0;
    for (auto& i : words_in_text)
    {
        if (i == word)
        {
            nr_of_app += 1;
        }
    }
    word_rank.insert(pair<string, int>(word, nr_of_app));
}
void create_vector_of_words(string sentence,vector<string> &words_in_text)
{
    istringstream sentence_to_parse(sentence);
    string word;
    while (getline(sentence_to_parse, word, ' ')) {
        words_in_text.push_back(word);
    }
}
int main()
{
    map<string, int> word_rank = {};
    vector<string> words_in_text;
    char word[100], sentence[100];
    cin.getline(sentence,sizeof(sentence));
    create_vector_of_words(sentence, words_in_text);
    for (auto& word : words_in_text)
    {
        count_word(word,words_in_text,word_rank);
    }
    for (auto& key_value : word_rank)
    {
        cout << key_value.first << " rank:" << key_value.second<<endl;
    }
}
