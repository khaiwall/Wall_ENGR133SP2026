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
import pandas as p
import math as m
import re


def load_samples():



    path = Path("Py4\sample_texts")
    files = list(path.iterdir())
    # print(files)
    openedFile = []
    for thisFile in range(len(files)):

        file_name = files[thisFile]
        with open(file_name, 'r', encoding='utf-8') as fid:
            fid.seek(0)
            all_data = fid.read()
            openedFile.append(all_data)
    return openedFile
    



def clean_text(currentSample):
    cleanSample= []
    for i in range(len(currentSample)):
        cleaned = re.sub(r"[^a-zA-Z0-9. ]", "", currentSample[i].replace("--", "").replace("\n", "")).lower()#Regex to remove anything that is not (^) a letter or number, and then converts uppercase to lowercase
    
        cleanSample.append(cleaned)

    return cleanSample

def main():
    samples = load_samples()
    dutch = samples[0]
    english = samples[1]
    french = samples[2]
    german = samples[3]
    italian = samples[4]
    spanish = samples[5]
    cleanSamples = clean_text(samples)

    print(cleanSamples[1])






# def plot_top_k(models, n, k=10):
#     fig, axs = plt.subplots(2, 3, figsize=(15, 10))

#     row = 0
#     col = 0

#     for language in models:
#         ax = axs[row][col]

#         n_gram = models[language]

#         # TODO :
#         top_ngrams = # set top_ngrams to be the sorted list of tuples (n-gram, frequency)
#         top_ngrams = top_ngrams[:k] # get the top k n-grams

#         grams = []
#         freqs = []
#         for gram, freq in top_ngrams:
#         # TODO :
#         # set grams and freqs to be lists of n-grams and frequencies from top_ngrams


#         ax.bar(grams, freqs)
#         # TODO :
#         # set title and axis labels
#         ax.tick_params(axis="x", rotation=45)

#         col += 1
#         # move to next row after 3 columns
#         if col == 3:
#             col = 0
#             row += 1

#     plt.tight_layout()
#     plt.show()


if __name__ == "__main__":
    main()
