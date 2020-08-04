/*
Write a program that gets from input a sentence, counts word frequencies, and prints one line for each word and frequencies
*/
import java.util.*;

class Solution {
	public static void count_word(String word,String[] sentence,Map<String, Integer> word_rank)
	{
		int nr_app=0;
		for (int i=0;i<sentence.length;i++)
		{
			if (sentence[i].equals(word))
			{
				nr_app+=1;
			}
		}
		word_rank.put(word,nr_app);
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Sentence=");
		String sentence=scanner.nextLine();
		Map<String, Integer> word_rank = new HashMap<String, Integer>();
		String[] words_in_text=sentence.split("\\s+");
		for (int i=0;i<words_in_text.length;i++)
		{
			count_word(words_in_text[i],words_in_text,word_rank);
		}
		for(String key : word_rank.keySet()) 
		{
			  System.out.println(key+":"+word_rank.get(key));
		}
	}
}
