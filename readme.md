# Atos In House Day "Spacy" Workshop
1. Create Atos inhouse day folder\
`$ mkdir atos_inhouse_day`
2. Open the folder \
`$ cd atos_inhouse_day`

3. Clone or Download this git repository
https://github.com/MarieGlas/atos_inhouse_day.git 

4. Create virtual environment\
`$ python3 -m venv myvenv`

5. Activate the virtual enviroment\
Windows:\
`C:\Users\Name\atos_inhouse_day> myvenv\Scripts\activate`\
macOS:\
`source myvenv/bin/activate`

6. Upgrade pip to the latest version\
`$ python -m pip install --upgrade pip`

7. Install needed packages & Django framework\
Windows:\
`C:\Users\Name\atos_inhouse_day> python -m pip install -r requirements.txt`\
macOs:\
`$ pip install -r requirements.txt`


 >  "spaCy is the best way to prepare text for deep learning. It interoperates seamlessly with TensorFlow, PyTorch, scikit-learn, Gensim and the rest of Python's awesome AI ecosystem. With spaCy, you can easily construct linguistically sophisticated statistical models for a variety of NLP problems"
https://spacy.io/ 

8. Install spacy\
`pip install -U spacy`\
`python -m spacy download en_core_web_sm`

9. Start migrations for creating sample database\
`python manage.py makemigrations`\
`python manage.py migrate`

10. Start the server\
`python manage.py runserver`

11. Open in your browser:\
The URL where the Django server is running (127.0.0.1)

12. Open in your code editor the folder\
`atos_inhouse_day`
13. Open `a_web/views.py`  you find missing code, try to complete them.\
After finishing open again: \
The URL where the Django server is running (127.0.0.1)
