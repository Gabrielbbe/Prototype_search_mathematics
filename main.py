import streamlit as st
import pickle
import os
from typing import Dict, List
from collections import OrderedDict
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def modify_key_values(list_of_dicts):
    modified_list = []
    for i, dictionary in enumerate(list_of_dicts):
        modified_dict = {}
        for key, value in dictionary.items():
            modified_key = f"{i}_{key}"
            modified_dict[modified_key] = value
        modified_list.append(modified_dict)
    return modified_list

def concatenate_dicts(list_of_dicts):
    concatenated_dict = {}
    for dictionary in list_of_dicts:
        concatenated_dict.update(dictionary)
    return concatenated_dict

def jaccard_similarity(str1: str, str2: str) -> float:
    set1 = set(str1)
    set2 = set(str2)
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

def sort_dict_by_similarity(input_str: str, dict_of_lists: Dict[str, List[str]]) -> Dict[str, List[str]]:
    similarity_scores = {}
    for key, value in dict_of_lists.items():
        similarity_scores[key] = max(jaccard_similarity(input_str, s) for s in value)
    
    sorted_dict = OrderedDict(sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True))
    return {key: dict_of_lists[key] for key in sorted_dict}

latex_dicts = []
latex_dicts_path = os.listdir('pickle_data/')

for latex_dict in latex_dicts_path:
    print(latex_dict)
    with open('pickle_data/'+latex_dict, 'rb') as pickle_file:
        ld = pickle.load(pickle_file)
    latex_dicts.append(ld)

latex_dicts = modify_key_values(latex_dicts)
latex_dicts = concatenate_dicts(latex_dicts)

user_input = st.text_input("Enter Latex code : ")

if user_input != None:

    results = sort_dict_by_similarity(user_input, latex_dicts)
    #results = pd.DataFrame(results)
    first_k = list(results.keys())[0]
    first_k = first_k[0]
    first_k = results[first_k+'_pagina0'][0]

    st.write(first_k)
    st.write(results)
    # for i, result in enumerate(results):
    #     st.write(f'{i} : {result}')     
