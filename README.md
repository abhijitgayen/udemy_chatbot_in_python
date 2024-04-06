# Chatbot using python(deep learning & NLP)

This is refence repo of the Udemy course `Chatbot using python (deep learning & NLP)`

link of the course [view](https://www.udemy.com/course/chatbot-using-python-deep-learning-nlp)

All the code in this video is available here. If you face any problems with your code, you can check it here.

Thank You. have a Nice day.


## Setup of the main project chatbot

### create vertual enviromet for this python project.
```
python -m venv myenv
```

### Active this vertual enviroment
For Windows:
```
myenv\Scripts\activate
```

For macOS and Linux:
```
source myenv/bin/activate
```

### deactivate virtual environment
```
deactivate
```

If you have problem use this [reference](https://github.com/abhijitgayen/udemy_chatbot_in_python/blob/main/basic_python/virtualenv.md)

### need to install project dependency
you need to install pytorch. accodding to your system.
https://pytorch.org/

for macbook and windows with cpu
```
pip install torch
```

for linux with cpu
```
pip3 install torch  --index-url https://download.pytorch.org/whl/cpu
```

Install other dependency like `numpy` and `nltk`
```
pip install -r requirements.txt
```

### go to main directory
```
cd chatbot
```

### To train this chatbot
```
python train.py
```

### To Run the main app
```
python app.py
```