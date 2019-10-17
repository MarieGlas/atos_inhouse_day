create Atos inhouse day folder\
`$ mkdir atos_inhouse_day`
`$ cd atos_inhouse_day`

create virtual environment
`$ python3 -m venv myvenv`

activate the virtual enviroment
windows:
`C:\Users\Name\djangogirls> myvenv\Scripts\activate`
macOS
`source myvenv/bin/activate`

upgrade pip to the latest version
`$ python -m pip install --upgrade pip`

install needed packages & django framework
windows 
`C:\Users\Name\atos_inhouse_day> python -m pip install -r requirements.txt`
macos
`$ pip install -r requirements.txt`


"spaCy is the best way to prepare text for deep learning. It interoperates seamlessly with TensorFlow, PyTorch, scikit-learn, Gensim and the rest of Python's awesome AI ecosystem. With spaCy, you can easily construct linguistically sophisticated statistical models for a variety of NLP problems"
https://spacy.io/

install spacy
`pip install -U spacy`
`python -m spacy download en_core_web_sm`

start migrations for creating sample database
`python manage.py makemigrations`
`python manage.py migrate`

start the server 
`python manage.py runserver`

open in your browser:
[DJANGO SERVER](http://127.0.0.1:8000)
The Django server is running

open in your code editor the folder 
`atos_inhouse_day`
In the file `a_web/views.py`  you find missing code, try to complete them. 
After finishing open the url again: 
http://127.0.0.1:8000
