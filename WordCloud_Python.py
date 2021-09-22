#!/usr/bin/env python
# coding: utf-8

# # Project - Word Cloud

# For this project, we will create a "word cloud" from a text by writing a script.  This script needs to process the text, remove punctuation, ignore case and words that do not contain all alphabets, count the frequencies, and ignore uninteresting or irrelevant words.  A dictionary is the output of the `calculate_frequencies` function.  The `wordcloud` module will then generate the image from your dictionary.

# For the input text of your script, you will need to provide a file that contains text only.  For the text itself, you can copy and paste the contents of a website you like.  Or you can use a site like [Project Gutenberg](https://www.gutenberg.org/) to find books that are available online.  You could see what word clouds you can get from famous books, like a Shakespeare play or a novel by Jane Austen. Save this as a .txt file somewhere on your computer.
# <br><br>
# Now you will need to upload your input file here so that your script will be able to process it.  To do the upload, you will need an uploader widget.  Run the following cell to perform all the installs and imports for your word cloud script and uploader widget.  It may take a minute for all of this to run and there will be a lot of output messages. But, be patient. Once you get the following final line of output, the code is done executing. Then you can continue on with the rest of the instructions for this notebook.
# <br><br>
# **Enabling notebook extension fileupload/extension...**
# <br>
# **- Validating: <font color =green>OK</font>**

# In[7]:


# Here are all the installs and imports you will need for your word cloud script and uploader widget

get_ipython().system('pip install wordcloud')
get_ipython().system('pip install fileupload')
get_ipython().system('pip install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# In[8]:


# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()


# The uploader widget saved the contents of your uploaded file into a string object named *file_contents* that your word cloud script can process.


# In[18]:


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",     "all", "any", "both", "each","so","one","on", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just","in","not","for","mr"]
    
    frequencies={}
    file_contents=file_contents.split()
    string=""
    
    for word in file_contents:
        string =''.join(ch for ch in word if ch.isalnum())
        if string.lower() not in uninteresting_words:
            
            if string.lower() not in frequencies:
                frequencies[string.lower()]=1
            else:
                frequencies[string.lower()]+=1
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


# In[19]:

# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
