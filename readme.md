Create Atos inhouse day folder\
`$ mkdir atos_inhouse_day`\
Open the folder \
`$ cd atos_inhouse_day`

Create virtual environment\
`$ python3 -m venv myvenv`

Activate the virtual enviroment\
Windows:\
`C:\Users\Name\djangogirls> myvenv\Scripts\activate`\
macOS:\
`source myvenv/bin/activate`

Upgrade pip to the latest version\
`$ python -m pip install --upgrade pip`

Install needed packages & Django framework\
Windows:\
`C:\Users\Name\atos_inhouse_day> python -m pip install -r requirements.txt`\
macOs:\
`$ pip install -r requirements.txt`


 >  "spaCy is the best way to prepare text for deep learning. It interoperates seamlessly with TensorFlow, PyTorch, scikit-learn, Gensim and the rest of Python's awesome AI ecosystem. With spaCy, you can easily construct linguistically sophisticated statistical models for a variety of NLP problems"
https://spacy.io/ 

Install spacy\
`pip install -U spacy`\
`python -m spacy download en_core_web_sm`

Start migrations for creating sample database\
`python manage.py makemigrations`\
`python manage.py migrate`

Start the server\
`python manage.py runserver`

Open in your browser:\
[DJANGO SERVER](http://127.0.0.1:8000)\
The Django server is running

Open in your code editor the folder 
`atos_inhouse_day`\
Open `a_web/views.py`  you find missing code, try to complete them.\
After finishing open the url again: \
http://127.0.0.1:8000
