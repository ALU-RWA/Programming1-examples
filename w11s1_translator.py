# This class will be a demo of a Translator class, which knows how to translate
# between 2 languages.
class Translator:
    def __init__(self, language1, language2):
        self.language1 = language1
        self.language2 = language2
        self.lang1_to_lang2 = {}
        self.lang2_to_lang1 = {}

    # Returns true if the translator knows the input language, false otherwise
    # This will make the following method easier to write
    def knows_language(self, language):
        return language == self.language1 or language == self.language2

    # Teach the dictionary a new word combination, you have to specify
    # which language each word is in.
    def teach(self, word1, lang_word_1, word2, lang_word_2):
        # First, let's make sure that the languages are valid.
        if not self.knows_language(lang_word_1) or not self.knows_language(lang_word_2):
            raise Exception("Unknown languages used, please use only " + self.language1 + " or " + self.language2)

        # Make sure that the languages are different
        if lang_word_2 == lang_word_1:
            raise Exception("That's not much of a translation is it?")

        # If our code gets here, then we know the languages are both valid, and different
        # Put the data in the appropriate dictionaries
        if lang_word_1 == self.language1:
            self.lang1_to_lang2[word1] = word2
            self.lang2_to_lang1[word2] = word1
        else:
            self.lang1_to_lang2[word2] = word1
            self.lang2_to_lang1[word1] = word2

    # Print the translation of a given word
    # Try to figure out if it's either language
    def translate(self, word):
        # This makes the assumption that we don't have the same word in both languages
        if word in self.lang1_to_lang2:
            return self.lang1_to_lang2[word]

        elif word in self.lang2_to_lang1:
            return self.lang2_to_lang1[word]

        else:
            return None # We failed to translate!

    # A lot of people were thinking about how to translate a whole sentence, here is an attempt:
    # This methods tries its best. If we can't translate a word in the sentence we keep the original word
    def translate_sentence(self, sentence):
        # First we split the sentence
        words = sentence.split(' ')
        output = ""
        for word in words:
            translation = self.translate(word)
            # If we can't translate it, keep the original word.
            # If we can translate the word, then concatenate it with the output
            if translation == None:
                output = output + " " + word
            else:
                output = output + " " + translation

        # Once we've gone through all the words, return the translated sentence:
        return output.strip()


#Demo time:
french_english_translator = Translator('french', 'english')
# Let's teach the translator a few words:
french_english_translator.teach('bonjour', 'french', 'hello', 'english')
french_english_translator.teach('monsieur', 'french', 'mister', 'english')
french_english_translator.teach('class', 'english', 'classe', 'french')
french_english_translator.teach('finished', 'english', 'terminee', 'french')

translated_sentence = french_english_translator.translate_sentence("bonjour monsieur gaidi")
print(translated_sentence)

# Note that it works the other way around as well:
back_to_original = french_english_translator.translate_sentence(translated_sentence)
print(back_to_original)

print(french_english_translator.translate_sentence("class is finished thank you"))