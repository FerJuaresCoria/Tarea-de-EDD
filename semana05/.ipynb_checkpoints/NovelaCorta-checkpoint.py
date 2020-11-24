from nltk.corpus import stopwords

class NovelaCorta():

    def __init__(self):
        pass

    def mostrar_stopwords(self):
        stop_words = frozenset(stopwords.words("spanish"))
        print(stop_words)

if __name__ == '__main__':
    a = NovelaCorta()
    a.mostrar_stopwords()
