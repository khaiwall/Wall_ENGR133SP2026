"""
Course Number: ENGR 13300
Semester: e.g. Spring 2026

Description:
    Build an n-gram frequency model based on data from other files

Assignment Information:
    Assignment:     py4 ind 1 
    Team ID:        LC1 - 03
    Author:         Khai, wall64@purdue.edu
    Date:           02/17/2026

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

""" Write any import statements here (and delete this line)."""

import matplotlib.pyplot as plt
from pathlib import Path
import re
import csv


def load_samples():



    # path = Path("Py4/sample_texts")
    path = Path("sample_texts")
    files = list(path.iterdir())
    nameList = ["dutch", "english", "french", "german", "italian", "spanish"]

    samples = {}
    for i, file_path in enumerate(files):
        with open(file_path, 'r', encoding='utf-8') as f:
            samples[nameList[i]] = f.read()
    
    return samples




def clean_text(currentSample):
    cleanSample= {}
    for language, text in currentSample.items():
        reduced = re.sub(r"[-]", "", text)
        cleaned_text = re.sub(r'\s{2,}', ' ', reduced)
        cleaned = re.sub(r"[^a-zA-Z ]", "", cleaned_text).lower()
    
        cleanSample[language] = (cleaned)

    return cleanSample
# def normalize_n_gram(oldGram):
#     reducedGrams = {}
#     for language, ngram_dict in oldGram.items():
#         total = sum(ngram_dict.values())
#         reducedGrams[language] = {gram: count / total for gram, count in ngram_dict.items()} 
#     return(reducedGrams)


def normalize_n_gram(oldGram):

    if all(isinstance(v, dict) for v in oldGram.values()):
        reducedGrams = {}
        for language, ngram_dict in oldGram.items():
            total = sum(ngram_dict.values())
            reducedGrams[language] = {gram: count / total for gram, count in ngram_dict.items()}
        return reducedGrams
    else:
        total = sum(oldGram.values())
        return {gram: count / total for gram, count in oldGram.items()}

def main():
    n = int(input("Enter the n-gram size to plot (1-5): "))
    grams = {}
    samples = load_samples()
    cleanSamples = clean_text(samples)
 
    for language, text in cleanSamples.items():
        grams[language] = create_n_gram(n, language, text) 
    normalGrams = normalize_n_gram(grams)
    plot_top_k(normalGrams, n, 10)

#CSV processing

    all_ngrams_per_language = {}

    for language, text in cleanSamples.items():
        all_ngrams_per_language[language] = {}
        for n in range(1, 6):
            ngram_dict = create_n_gram(n, language, text)
            normalized = normalize_n_gram({language: ngram_dict})
            all_ngrams_per_language[language][n] = normalized[language]

    for language, ngram_data in all_ngrams_per_language.items():
        filename = f"py4_ind_1_{language}.csv"
        
        with open(filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['n', 'n-gram', 'frequency'])  # header
            
            for n in range(1, 6):
                ngrams = ngram_data[n]
                for gram_tuple, freq in ngrams.items():
                    gram_str = ''.join(gram_tuple)
                    writer.writerow([n, gram_str, freq])
        

def create_n_gram(n, name, currentTexts):
   
    if isinstance(currentTexts, dict):
        if name not in currentTexts:
            raise ValueError(f"Language '{name}' not found in input")
        text = currentTexts[name]
    else:
        text = currentTexts

    ngrams = {}
    for i in range(len(text) - n + 1):
        gram = text[i:i+n]  # slice as string
        ngrams[gram] = ngrams.get(gram, 0) + 1

    return ngrams

def plot_top_k(models, n, k=10):
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))


    row = 0
    col = 0

    for language in models:
        ax = axs[row][col]

        n_gram = models[language]

        # TODO :

        sorted_list = sorted(n_gram.items(), key=lambda item: item[1], reverse=True)
        top_ngrams = sorted_list[:k] # get the top k n-grams

        grams = []
        freqs = []

        for gram, freq in top_ngrams:
            grams.append(''.join(gram))
            freqs = [freq for g, freq in top_ngrams]


        ax.bar(grams, freqs)
        # TODO :
        ax.set_ylabel("frequency")
        ax.set_xlabel(f"{n}-grams")
        ax.set_title(language)
        ax.tick_params(axis="x", rotation=45)

        col += 1
        # move to next row after 3 columns
        if col == 3:
            col = 0
            row += 1

    plt.tight_layout()
    # plt.show()




    
if __name__ == "__main__":
    main()
