"""
Course Number: ENGR 13300
Semester: e.g. Spring 2026

Description:
    Build an n-gram frequency model based on data from other files

Assignment Information:
    Assignment:     py4 ind 2 
    Team ID:        LC1 - 03
    Author:         Khai, wall64@purdue.edu
    Date:           02/19/2026

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
import os


def create_models():



    path = Path("Py4/unknown_texts")
    # path = Path("unknown_texts")
    files = list(path.iterdir())
    nameList = ["unknown_1", "unknown_2", "unknown_3"]

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



def create_n_gram(n, name, currentTexts):
   
    if isinstance(currentTexts, dict):
        if name not in currentTexts:
            raise ValueError(f"Language '{name}' not found in input")
        text = currentTexts[name]
    else:
        text = currentTexts

    ngrams = {}
    for i in range(len(text) - n + 1):
        gram = text[i:i+n]
        ngrams[gram] = ngrams.get(gram, 0) + 1

    return ngrams





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
    


def all_n_grams(cleanSamples):
    
    all_ngrams_per_language = {}

    for name, text in cleanSamples.items():
        all_ngrams_per_language[name] = {}
        for n in range(1, 6):
            ngram_dict = create_n_gram(n, name, text)
            normalized = normalize_n_gram({name: ngram_dict})
            all_ngrams_per_language[name][n] = normalized[name]
    return all_ngrams_per_language


def load_from_csv():
    folder_path = Path("Py4csvs")
    nameList = ["dutch", "english", "french", "german", "italian", "spanish"]

    data_dict = {}
    for count, filename in enumerate(os.listdir(folder_path)):
        if filename.endswith(".csv"):
            full_path = folder_path / filename
            data_dict[nameList[count]] = {}
            with open(full_path, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    n = int(row[0])
                    gram = row[1]
                    freq = float(row[2])
                    if n not in data_dict[nameList[count]]:
                        data_dict[nameList[count]][n] = {}
                    data_dict[nameList[count]][n][gram] = freq
    return data_dict

def n_gram_dist(language, unknown, n):
    total_diff = 0
    lang_ngrams = language.get(n, {})
    unk_ngrams = unknown.get(n, {})
    all_grams = set(lang_ngrams.keys()) | set(unk_ngrams.keys())
    for gram in all_grams:
        total_diff += abs(lang_ngrams.get(gram, 0) - unk_ngrams.get(gram, 0))
    return total_diff

def score_language(languages, unknown, n):
    scores = {}
    for lang_name, lang_dict in languages.items():
        scores[lang_name] = n_gram_dist(lang_dict, unknown, n)

    return scores

def score_separation(distance_scores):
    separation_scores = {}
    languages = list(distance_scores.keys())
    n = len(languages)

    for lang in languages:
        lang_score = distance_scores[lang]
        # Sum of absolute differences with all other languages
        total_diff = sum(abs(lang_score - distance_scores[other_lang]) 
                         for other_lang in languages if other_lang != lang)
        # Divide by (n - 1) as per formula
        separation_scores[lang] = total_diff / (n - 1)
    print(separation_scores)
    return separation_scores

def main():
    unknown_samples = create_models()
    unknownCleanSamples = clean_text(unknown_samples)
    unknownGrams = all_n_grams(unknownCleanSamples)
    language_csvs = load_from_csv()
    counters = 0
    print("Unknown Language File Options\n")

    for name, text in unknownGrams.items():
        counters +=1
        print(f"{counters}. {name:<5}")

    currentFile = input("Select a file to analyize: ")
    scores_by_n = {}

    for n in range(1, 6):
        # compute distance scores for this n
        distance_scores = score_language(language_csvs, unknownGrams[currentFile], n)
        # compute separation for this n
        separation_scores = score_separation(distance_scores)
        # store in dictionary by n
        scores_by_n[str(n)] = separation_scores

    plot_separation_vs_n(scores_by_n, currentFile)




import matplotlib.pyplot as plt

def plot_separation_vs_n(scores_by_n, name):
    fig, axs = plt.subplots(2, 3, figsize=(15, 10), sharey=True)

    n_values = sorted([int(n) for n in scores_by_n.keys()])

    # languages from the first n entry (assumes all n have same languages)
    first_n = str(n_values[0])
    languages = sorted(scores_by_n[first_n].keys())

    row = 0
    col = 0

    for language in languages:
        ax = axs[row][col]

        # collect y-values (scores) in order of n
        y_scores = [scores_by_n[str(n)][language] for n in n_values]

        # plot n_values (x) vs y_scores (y)
        ax.plot(n_values, y_scores, 'bo-', label=language)

        ax.set_xticks(n_values)
        ax.set_xlabel("n-gram size (n)")
        ax.set_ylabel("Separation Score")
        ax.set_title(language)

        col += 1
        if col == 3:
            col = 0
            row += 1

    plt.suptitle(f"{name} Language Separation", fontsize=16)
    plt.tight_layout()
    plt.show()

    
if __name__ == "__main__":
    main()
