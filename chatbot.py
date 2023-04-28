### Importing the libraries
import gpt_2_simple as gpt2
import re


class Chatbot:

    def __init__(self, response=None):
        self.sees = gpt2.start_tf_sess()
        gpt2.load_gpt2(self.sees)

    
        ############################# Help Bot ############################

    def help_bot(self, text):

        # Generate the response
        self.text1 = gpt2.generate(
            self.sees,
            length=100,
            include_prefix=False,
            temperature=0.7,
            prefix=text,
            nsamples=1,
            batch_size=1,
            return_as_list=True,
            top_k=100,
        )

        ############################## Format text #########################
        ####################### Objectives ####################
        # Replacing unwanted symbols
        # Capitalize each sentence
        # Removing the input prefix
        # Correcting the grammer using Gramformer

        self.sentence = self.text1[0].split(". ")
        # Removing the input prefix
        self.sentence[0] = self.sentence[0].split("? ")[-1]
        self.corrected_sentence = []
        for i in range(len(self.sentence) - 1):
            # Replacing unwanted symbols
            self.sentence[i] = self.sentence[i].replace("*", ",")
            self.sentence[i] = self.sentence[i].replace(";", ",")
            # Capitalize each sentence
            self.corrected_sentence.append(self.sentence[i].capitalize())

        self.l = ". ".join(self.corrected_sentence) + "."

        for i in range(len(self.l)):
            if ord(self.l[i]) >= 48:
                start = i
                break

        self.l1 = self.l[start:]
        if start > 0:
            self.txt1 = self.l1.split(". ")
            for i in range(len(self.txt1)):
                if ord(self.txt1[i][0]) >= 97:
                    # Capitalize each sentence
                    self.txt1[i] = self.txt1[i].capitalize()
                    break

            ###################### Correcting the Grammer of the sentence ####################

            self.l2 = ". ".join(self.txt1)
            return self.l2
        
        return self.l1

    

    
