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

    # # uncomment all lines below <fill in> missing items (command + / (macOS))
    # # create a list with doc sentences
    ## HINT: https://spacy.io/usage/spacy-101#lightning-tour-tokens-sentences
    # sentences = list(doc<fill in>)
    # for sentence in sentences:
    #     sentence_list.append(sentence)
    #
    # # An individual token — i.e. a word, punctuation symbol, whitespace, etc
    # # Create for token loop
    # # HINT:  https://spacy.io/api/token#attributes
    # for <fill in> in doc:
    #     token_list.append(token)
    #     # check if token is stop word
    #     if token<fill in>:
    #         stopwords_list.append(token)
    #     # check if token is non stop word
    #     if not token<fill in>:
    #         non_stopwords_list.append(token)
    #
    #     #check if token pos is verb
    # # HINT: https://spacy.io/usage/linguistic-features#pos-tagging
    #     if token<fill in> == "VERB":
    #         verbs_list.append(token)
    #
    # # append all noun chunks from text to list
    # # HINT: https://spacy.io/usage/linguistic-features#noun-chunks
    # for chunk in doc<fil in>:
    #     noun_phrases_list.append(chunk.text)
    #
    # # append all entity text & labels from  doc to list
    # # HINT FEATURES: https://spacy.io/
    # for entity in doc<fill in>:
    #     entitylist = (entity<fill in>, entity.<fill in>)
    #     entity_txt_lbl_list.append(entitylist)
    #
    # # put lists & text in context for template
    context = {
        'text': doc,
        # uncomment context items  <fill in> missing items (command + /) macOs)
        # 'sentence_list': <fill in>,
        # 'token_list': <fill in>,
        # 'stopwords_list': <fill in>,
        # 'nonstopwords_list': <fill in>,
        # 'verbs_list': <fill in>,
        # 'nounphrases_list': <fill in>,
        # 'entity_txt_lbl_list':  <fill in>
    }

    return render(request, 'a_web/atosday.html', context)
