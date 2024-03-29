from django.shortcuts import render
import spacy


def atos_inhouse(request):
    nlp = spacy.load("en_core_web_sm")
    text = ("Atos’ history spans a century, from Fredrik Rosing Bull first creating the tabulating machine to Europe’s"
            "number one digital services provider."
            " Every day our 110,000 people in 73 countries are developing and implementing innovative digital solutions"
            "that support the business transformation"
            "of clients and address the environmental and social challenges we all face."
            " Atos is the Worldwide Information Technology Partner for the Olympic & Paralympic Games and operates under"
            " the brands Atos, Atos Syntel, and Unify. Atos is a SE (Societas Europaea),"
            " listed on the CAC40 Paris stock index")
    doc = nlp(text)
    stopwords_list = []
    token_list = []
    sentence_list = []
    non_stopwords_list = []
    noun_phrases_list = []
    verbs_list = []
    entity_txt_lbl_list = []
    template = 'a_web/atosday.html'

    # create a list with document sentences
    sentences = list(doc.sents)
    for sentence in sentences:
        sentence_list.append(sentence)

    # An individual token — i.e. a word, punctuation symbol, whitespace, etc
    for token in doc:
        token_list.append(token)
        # check if token is stop word
        if token.is_stop:
            stopwords_list.append(token)
        # check if token is non stop word
        if not token.is_stop:
            non_stopwords_list.append(token)

        # check if token pos is verb
        if token.pos_ == "VERB":
            verbs_list.append(token)

    # append all noun chunks from text to list
    for chunk in doc.noun_chunks:
        noun_phrases_list.append(chunk.text)

    # append all entity text & labels from  doc to list
    for entity in doc.ents:
        entitylist = (entity.text, entity.label_)
        entity_txt_lbl_list.append(entitylist)

    # put lists & text in context for template
    context = {
        'text': doc,
        'sentence_list': sentence_list,
        'token_list': token_list,
        'stopwords_list': stopwords_list,
        'nonstopwords_list': non_stopwords_list,
        'verbs_list': verbs_list,
        'nounphrases_list': noun_phrases_list,
        'entity_txt_lbl_list': entity_txt_lbl_list
    }

    return render(request, 'a_web/atosday.html', context)
