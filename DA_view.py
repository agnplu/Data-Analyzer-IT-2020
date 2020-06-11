# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:54:40 2020

@author: Agnieszka
"""
import tkinter as tk
import tkinter.messagebox

initial_message = "Welcome to Data Analyzer - a tool for analyzing your vocabulary! \n\n\n1. To begin, open a file from File > Open file. The program will only analyze files written in English. \n\n2. Having done it, you can display the regular file as well as the annotated version by clicking the 'Show annotated' button above. \n\n3. On the right side you can see the number of types, tokens and the type-token ratio of your text. If you want to learn more about it, read a short description by hovering over the little question mark. \n\n4. To go to a more detailed analysis, use 'Analyze' found in the menu. There you will be able to choose between particular parts of speech to obtain a more in-depth analysis of your file. \n\n 5. You can find additional information about the program and my email address in the 'Info' menu. \n\n\n Have fun!"
program_information = "In Data Analyzer, NLTK is used to categorize the user’s input into categories corresponding to parts of speech (POS) of particular tokens found in the text. Such a solution enables conducting separate analyses of four parts of speech (nouns, verbs, adjectives, and adverbs) which constitute a group of the so-called content words – words that have semantic content and contribute to the meaning of the sentence in which they occur. \n\nHaving chosen a particular part of speech from the Analysis Menu, the user will be able to inspect the most frequent words categorized to one the four groups.\n\nSuch an analysis is used when inspecting one’s style of writing as well as in historical and comparative linguistics (to trace particular lexical trends in a given period of time). For students or writers, the analysis might be useful in that it lists a range of words which might be overused by the author in a particular text."
nltk_information = "Natural Language Toolkit (NLTK) is a free, open source, platform for building Python programs to work with human language data. It provides a range of interfaces such as text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning. Its implementation to a Python program allows for working with corpora, categorizing text and analyzing its linguistic structures. Programs using NLTK might prove useful for individuals working in the field of linguistics, as well as for students, educators, researchers, and engineers."
contact_information = "My name is Agnieszka Pludra and I am a 2BA English Linguistics student at Adam Mickiewicz University in Poznań. \nIf you have any questions or suggestions, send me an email!"
tags = "ADJ \nADP \nADV \nCONJ \nDET \nNOUN \nNUM \nPRT \nPRON \nVERB \nX "
explanations = "Adjective \nAdposition \nAdverb \nConjugation \nDeterminer/Article \nNoun \nNumeral \nParticle \nPronoun \nVerb \nOther"
type_token_information = "Type-token ratio (TTR) is the total number of types (unique words) divided by the total number of tokens (all words). The ratio is a useful measure of text complexity - the closer it is to is to 1, the greater the lexical richness of the segment. TTR allows for a preliminary analysis of any sample - it reveals whether the sample was produced in the writing or spoken mode (speech is characterized by considerably less variation, thus lower TTR) and helps assume the age of the speaker (children's speech is much less diverse than adults' speech)."

def program_info():
    top = tk.Toplevel(bg="gray75")
    top.title("About the program")
    top.geometry("600x400+330+200")
    info_label = tk.Label(top, text = program_information, bg="gray75", font=9, wraplength=550, fg ="white", padx=10, pady=10)
    info_label.pack(padx=10, pady=10, fill=tk.BOTH)
    button_close = tk.Button(top, text="Close", command=top.destroy, bg="LightSkyBlue3", fg="white")
    button_close.pack(padx=10, pady=10)

def nltk_info():
    top = tk.Toplevel(bg="gray75")
    top.title("About NLTK")
    top.geometry("600x250+330+200")
    info_label = tk.Label(top, text=nltk_information, font=9, wraplength=550, bg="gray75", fg="white", padx=10, pady=10)
    info_label.pack(padx=10, pady=10, fill=tk.BOTH)
    button_close = tk.Button(top, text="Close", command=top.destroy, bg="LightSkyBlue3", fg="white")
    button_close.pack(padx=10, pady=10)

def contact_info():
    top = tk.Toplevel(bg="gray75")
    top.title("Contact the author")
    top.geometry("600x250+330+200")
    contact_label = tk.Label(top, text=contact_information, bg="gray75", font=10, fg="white", wraplength=550, padx=10, pady=10)
    contact_label.pack(padx=10, pady=25, fill=tk.BOTH)
    email_label = tk.Label(top, text="agnplu@st.amu.edu.pl", bg="LightSkyBlue3", font=10, fg="white", pady=10, borderwidth=1, relief="solid")
    email_label.pack(padx=10, pady=(0,15), fill=tk.BOTH)
    button_close = tk.Button(top, text="Close", command=top.destroy, bg="LightSkyBlue3", fg="white")
    button_close.pack(padx = 10, pady = 20)
    
def stringify(sorted_list):
    string = ""
    for word, frequency in sorted_list:
        string += word+" -- "+str(frequency)
        string += "\n"
    return string[:-1]

class View:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.geometry("800x600+200+50")
        self.root.title("Data analyzer")
        self.right_frame = None
        self.alternative_frame = None
        self.initGUI()

    def initGUI(self):
        self.init_vars()
        self.init_menu()
        self.init_left()
        self.init_right()      

    def init_vars(self):
        # main text
        self.main_text = tk.StringVar(self.root)
        self.set_text(initial_message)
        self.annotated_text = tk.StringVar(self.root)
        self.set_annotated(initial_message)
        # number of all words
        self.tokens = tk.IntVar()
        self.tokens_text = tk.StringVar(self.root)
        self.set_tokens(0)
        # number of unique words
        self.types = tk.IntVar(self.root)
        self.types_text = tk.StringVar(self.root)
        self.set_types(0)
        # types to tokens
        self.types_to_tokens = tk.DoubleVar(self.root)
        self.types_to_tokens_text = tk.StringVar(self.root)
        self.set_t2t(0)
        # variable to CheckButton
        self.var = tk.IntVar(self.root)
        # hovering variable
        self.var2 = tk.IntVar(self.root)

    def init_menu(self):
        menubar = tk.Menu(self.root)

        filemenu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Open file", command=self.controller.open_file)
        filemenu.add_command(label="Close file", command=self.controller.close_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)

        analysismenu = tk.Menu(menubar)
        menubar.add_cascade(label="Analysis", menu=analysismenu)
        analysismenu.add_command(label="Nouns", command=self.controller.nouns_info)
        analysismenu.add_command(label="Verbs", command=self.controller.verbs_info)
        analysismenu.add_command(label="Adjectives", command=self.controller.adj_info)
        analysismenu.add_command(label="Adverbs", command=self.controller.adv_info)
        analysismenu.add_separator()
        analysismenu.add_command(label="Quit analysis", command=self.init_right)

        infomenu = tk.Menu(menubar)
        menubar.add_cascade(label="Info", menu=infomenu)
        infomenu.add_command(label="About the program", command=program_info)
        infomenu.add_command(label="About NLTK", command=nltk_info)
        infomenu.add_command(label="Contact the author", command=contact_info)
        self.root.configure(menu=menubar)

    def init_left(self):
        left_frame=tk.Frame(self.root)
        left_frame.configure(bg="gray97")

        canvas=tk.Canvas(left_frame)
        scrollbar = tk.Scrollbar(left_frame, orient="vertical", command=canvas.yview)
        scrollable_frame=tk.Frame(canvas)
        scrollable_frame.config(bg="gray97")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0,0), window=scrollable_frame, anchor=tk.NW)
        canvas.configure(yscrollcommand=scrollbar.set)
        self.text_display=tk.Label(scrollable_frame, textvariable=str(self.main_text), width=40, bg="LightSkyBlue3", wraplength=360, font=10, fg="white", padx=10, pady=10, justify=tk.LEFT)
        self.text_display.pack(padx=10, pady=10)

        annotate_checkbutton=tk.Checkbutton(left_frame, text="Show annotated", variable=self.var, onvalue=1, offvalue=0, fg="white", bg="gray75", selectcolor="gray80")
        annotate_checkbutton.pack(padx=10, pady=10)
        annotate_checkbutton.bind("<Button-1>", self.controller.toggle_annotated)

        left_frame.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.BOTH)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def init_right(self):
        if self.alternative_frame!=None:
            self.alternative_frame.pack_forget()
            self.alternative_frame = None

        self.right_frame = tk.Frame(self.root, bg="gray97")        

        type_label=tk.Label(self.right_frame, width=40, bg="gray75", textvariable=str(self.types_text), font=9, fg="white", padx=5, pady=10)
        type_label.pack(padx=10, pady=(10,0), fill=tk.BOTH)

        token_label=tk.Label(self.right_frame, width=40, bg="gray75", textvariable=str(self.tokens_text), font=9, fg="white", padx=5, pady=10)
        token_label.pack(padx=10, pady=(0,2), fill=tk.BOTH)

        type_to_token_label=tk.Label(self.right_frame, width=40, bg="gray75", textvariable=str(self.types_to_tokens_text), font=9, fg="white", padx=5, pady=10)
        type_to_token_label.pack(padx=10, fill=tk.BOTH)

        info_popup=tk.Button(type_to_token_label, text="?", bg="LightSkyBlue3", fg="white")
        info_popup.pack(anchor=tk.E, padx=10, pady=10)
        info_popup.bind("<Enter>", self.show_info)
        info_popup.bind("<Leave>", self.hide_info)

        type_token_explanation=type_token_information
        self.information_type_token=tk.Label(self.right_frame, bg="gray97", fg="gray97", text=type_token_explanation, padx=10, pady=10, width=60, wraplength=320)
        self.information_type_token.pack(padx=10, pady=(0,5))

        self.show_tags_label=tk.Label(self.right_frame, width=60, text="Annotation tags:", bg="gray97", fg="gray97", padx=10, pady=10)
        self.show_tags_label.pack(padx=10)

        self.tags_label=tk.Label(self.right_frame, width=20, text=tags, bg="gray97", fg="gray97", padx=10, pady=10, justify=tk.RIGHT)
        self.tags_label.pack(padx=(10, 0), pady=(0, 25), side=tk.LEFT)
        self.explanations_label=tk.Label(self.right_frame, width=35, text=explanations, bg="gray97", fg="gray97", padx=10, pady=10, justify=tk.LEFT)
        self.explanations_label.pack(padx=(1, 10), pady=(0, 25), side=tk.RIGHT)
        self.right_frame.pack(padx=10, pady=10, side=tk.RIGHT, fill=tk.Y)

    def show_info(self, event):
        self.information_type_token.configure(bg="white", fg="gray55", borderwidth=1, relief="groove")

    def hide_info(self, event):
        self.information_type_token.configure(bg="gray97", fg="gray97", borderwidth=0)
           
    def alternate_right(self, pos, number, sorted_list, token_count):
        if self.right_frame!=None:
            self.right_frame.pack_forget()
            self.right_frame = None
        if self.alternative_frame!=None:
            self.alternative_frame.pack_forget()
            self.alternative_frame=None

        self.alternative_frame = tk.Frame(self.root, bg="gray97")                
        
        name_label=tk.Label(self.alternative_frame, text=pos, bg="LightSkyBlue3", fg="white", font=9, padx=10, pady=10, width=50)
        name_label.pack(padx=10, pady=(10,0))
        
        total_text="Total number: "+str(number)+" (out of {}".format(str(self.tokens.get()))+" words in total)" 
        total_frequency_label = tk.Label(self.alternative_frame, text=total_text, bg="gray75", fg="white", font=9, padx=10, pady=10, width=50)
        total_frequency_label.pack(padx=10, pady=2)

        sorted_info_label=tk.Label(self.alternative_frame, text="20 most frequent:", bg="gray75", fg="white", font=9, padx=10, pady=10, width=50)
        sorted_info_label.pack(padx=10)
        
        sorted_frequency_label=tk.Label(self.alternative_frame, text=stringify(sorted_list[:20]), bg="gray75", fg="white", font=9, padx=10, pady=10, width=50, justify=tk.LEFT)
        sorted_frequency_label.pack(padx=10, pady=2)

        back_to_main=tk.Button(self.alternative_frame, text="Quit analysis", command=self.init_right, bg="LightSkyBlue3", fg="white")
        back_to_main.pack(padx=(10,2), pady=2, side=tk.LEFT)
        save=tk.Button(self.alternative_frame, text="Save all frequencies", command=lambda: [self.controller.save_frequencies(pos, str(sorted_list)), self.controller.saved_info()], bg="LightSkyBlue3", fg="white")
        save.pack(padx=(2,10), pady=2, side=tk.RIGHT)
       
        self.alternative_frame.pack(padx=10, pady=10, side=tk.RIGHT, fill=tk.Y)
            
    def set_text(self, text):
        self.main_text.set(text)
    def set_annotated(self, annotated):
        self.annotated_text.set(annotated)
    def set_tokens(self, tokens):
        self.tokens.set(tokens)
        self.tokens_text.set("Number of tokens: "+str(self.tokens.get()))
    def set_types(self, types):
        self.types.set(types)
        self.types_text.set("Number of types: "+str(self.types.get()))
    def set_t2t(self, t2t):
        self.types_to_tokens.set(t2t)
        self.types_to_tokens_text.set("Type-to-token ratio: "+str(self.types_to_tokens.get()))

    def use_annotated(self):
        self.text_display.configure(textvariable=str(self.annotated_text))
        self.show_tags_label.configure(bg="LightSkyBlue3", fg="white")
        self.tags_label.configure(bg="gray75", fg="white")
        self.explanations_label.configure(bg="gray75", fg="white")

    def use_raw(self):
        self.text_display.configure(textvariable=str(self.main_text))
        self.show_tags_label.configure(bg="gray97", fg="gray97")
        self.tags_label.configure(bg="gray97", fg="gray97")
        self.explanations_label.configure(bg="gray97", fg="gray97")

    
