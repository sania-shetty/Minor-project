import spacy,coreferee
import re
cor=spacy.load("en_core_web_sm")
cor.add_pipe("coreferee")
class coref():
    def __init__(self,file):
        self.file=file
    def coref(self):
        with open(self.file,"r") as read_file:
            dirty_text=read_file.read()
        self.dirty_text=dirty_text
        cor_text=cor(dirty_text)
        self.cor_text=cor_text
        chains=cor_text._.coref_chains
        chains.print()
        self.chains=chains
    def replace_coref(self):
        dirty_text=self.dirty_text
        regular=self.dirty_text
        cor_text=self.cor_text
        chains=self.chains
        for i in range(len(chains)):
            resolve=chains.resolve(cor_text[chains[i][1][0]])
            """ print(resolve[0]) """
            for mention in range(1,len(chains[i])):
                """ print(str(cor_text[chains[i][mention][0]]))
                print(str(resolve[0])) """
                dirty_text=dirty_text.replace(str(cor_text[chains[i][mention][0]]),str(resolve[0]))
                regular=re.sub(r'\b'+str(cor_text[chains[i][mention][0]])+r'\b',str(resolve[0]),regular,count=1)
                """ print(dirty_text) """
        with open("coref.txt","w") as cleaned:
            cleaned.write(dirty_text)
        with open("regular.txt","w") as reg:
            reg.write(regular)

o=coref("text.txt")
o.coref()
o.replace_coref()

        
        
    
