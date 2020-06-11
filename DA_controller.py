# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:57:38 2020

@author: Agnieszka
"""
import DA_model as m
import DA_view as v 
import tkinter as tk
import webbrowser
from tkinter import filedialog
import tkinter.messagebox


class Controller:
    def __init__(self):
        self.document = m.Document()
        self.view = v.View(self)

    def start(self):
        self.open_window()
        self.view.root.mainloop()  
        
    def open_website(self):
        return webbrowser.open("https://www.nltk.org/install.html")

    def open_window(self):
        self.view.root.withdraw()
        top = tk.Toplevel()
        top.geometry("600x250+330+200")
        top.title("Install NLTK")
        info = "For the program to run you must install the Natural Language Toolkit (NLTK). \n\nHave you installed it?"
        initial_label = tk.Label(top, text=info, padx=20, pady=20)
        initial_label.pack(padx=30, pady=30)
        button_yes = tk.Button(top, bg="LightSkyBlue3", fg="white", text="Yes, run the program",
                               command=lambda: [top.destroy(), self.view.root.deiconify()])
        button_yes.place(relx=0.3, rely=0.7)
        button_no = tk.Button(top, bg="LightSkyBlue3", fg="white", text="No, I will do it now",
                              command=lambda: [self.open_website(), self.view.root.destroy()])
        button_no.place(relx=0.53, rely=0.7)


    def open_file(self):
        if self.view.types.get() != 0:
            self.close_file()
        path = filedialog.askopenfilename(filetypes=[("Text files", ".txt"), ("All files", ".*")])
        self.document.load_file(path)

        self.view.set_text(self.document.text)
        self.view.set_annotated(self.document.annotate())
        self.view.set_types(self.document.count_unique())
        self.view.set_tokens(self.document.count_tokens())
        self.view.set_t2t(self.document.type2token_ratio())
        
    def save_frequencies(self, name, freqs):
        f = open(name+"_frequencies.txt", "w")
        f.write(freqs)
        f.close()
        
    def nouns_info(self):
        number_of_nouns, nouns = self.document.pos("N")
        number_of_tokens = self.document.count_tokens()
        self.view.alternate_right("NOUNS", number_of_nouns, nouns, number_of_tokens)
    def verbs_info(self):
        number_of_verbs, verbs = self.document.pos("V")
        number_of_tokens = self.document.count_tokens()
        self.view.alternate_right("VERBS", number_of_verbs, verbs, number_of_tokens)
    def adj_info(self):
        number_of_adjectives, adjectives = self.document.pos("ADJ")
        number_of_tokens = self.document.count_tokens()
        self.view.alternate_right("ADJECTIVES", number_of_adjectives, adjectives, number_of_tokens)
    def adv_info(self):
        number_of_adverbs, adverbs = self.document.pos("ADV")
        number_of_tokens = self.document.count_tokens()
        self.view.alternate_right("ADVERBS", number_of_adverbs, adverbs, number_of_tokens) 
    
    def saved_info(self):
        tk.messagebox.showinfo("Saved file", "Saved to the current directory")
    
    def close_file(self):
        question_box = tk.messagebox.askquestion("Close file", "Are you sure you want to close this file?")
        if question_box == 'no':
            return
        self.document.close_file()
        self.view.set_text(v.initial_message)
        self.view.set_annotated(v.initial_message)
        self.view.set_types(0)
        self.view.set_tokens(0)
        self.view.set_t2t(0.0)

    def toggle_annotated(self, event):
        if self.view.var.get() == 0:
            self.view.use_annotated()
        else:
            self.view.use_raw()
            