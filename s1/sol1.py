import nltk
from nltk.corpus import stopwords
from collections import Counter

# nltk.download("punkt")
# nltk.download("stopwords")

def count_words(filename):
    try:
        with open(filename, "r") as file:
            text = file.read().lower()
            words = nltk.word_tokenize(text)
            words = [word for word in words if word.isalpha()]
            words = [word for word in words if word not in stopwords.words("english")]
            word_counts = Counter(words)
            return word_counts.most_common(5)
    except FileNotFoundError:
        print("File Not Found")
        return []
    except Exception as e:
        print("Error occurred: ", str(e))
        return []

file_path = input("Enter Path of text file: ")
top_words = count_words(file_path)

if top_words:
    print("Top 5 most frequently occurring words:")
    for word, count in top_words:
        print(f"{word} : {count}")
else:
    print("No results found")
    


"""
Explanation : 

1. Importing Libraries:
   - The code begins by importing the necessary libraries: `nltk`, `stopwords` from `nltk.corpus`, and `Counter` from `collections`.
   - `nltk` (Natural Language Toolkit) is a library for natural language processing tasks.
   - `stopwords` is a module within `nltk.corpus` that provides a list of common stopwords.
   - `Counter` is a class from the `collections` module used for counting the frequency of elements.

2. Commented NLTK Resource Downloads:
   - The code includes commented lines that would download the required NLTK resources (`punkt` and `stopwords`). Since you have already downloaded them, they can be left commented.

3. Defining the `count_words` Function:
   - The `count_words` function takes a filename as input and returns the five most common words in the file.
   - It begins by opening the file using a `with` statement to ensure proper file handling.
   - The text from the file is read and converted to lowercase using the `lower()` method.
   - The text is tokenized into individual words using `nltk.word_tokenize`.
   - The list of words is filtered to include only alphabetic words using a list comprehension and the `isalpha()` method.
   - The remaining words are further filtered to remove stopwords by checking if they are not in the list of English stopwords obtained from `stopwords.words("english")`.
   - The frequency count of each word is calculated using the `Counter` class.
   - Finally, the function returns the five most common words as a list of tuples using the `most_common()` method of `Counter`.

4. User Input :
   - The user is prompted to enter the path of the text file they want to analyze.
   - The `count_words` function is called with the provided file path.
   - The result, stored in the `top_words` variable, is a list of tuples where each tuple contains a word and its frequency count.

5. Printing the Results:
   - If the `top_words` list is not empty (indicating there are results), the code prints the header "Top 5 most frequently occurring words:".
   - A loop is used to iterate over each word and count in the `top_words` list.
   - The word and its count are printed using f-string formatting.
   - If the `top_words` list is empty, indicating no results, the code prints "No results found.”



"""
