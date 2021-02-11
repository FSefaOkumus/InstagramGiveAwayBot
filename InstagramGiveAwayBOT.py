#!/usr/bin/env python
# encoding: utf-8
"""

Created by Sefa Okumuş on 2020-06-01.
"""

from tkinter import *
import sys
import os
import tkinter
import tkinter.ttk


__version__ = "1.0"

tkinter_umlauts=['odiaeresis', 'adiaeresis', 'udiaeresis', 'Odiaeresis', 'Adiaeresis', 'Udiaeresis', 'ssharp']

class AutocompleteEntry(tkinter.Entry):
        """
        Subclass of Tkinter.Entry that features autocompletion.

        To enable autocompletion use set_completion_list(list) to define
        a list of possible strings to hit.
        To cycle through hits use down and up arrow keys.
        """
        def set_completion_list(self, completion_list):
                self._completion_list = sorted(completion_list, key=str.lower) # Work with a sorted list
                self._hits = []
                self._hit_index = 0
                self.position = 0
                self.bind('<KeyRelease>', self.handle_keyrelease)

        def autocomplete(self, delta=0):
                """autocomplete the Entry, delta may be 0/1/-1 to cycle through possible hits"""
                if delta: # need to delete selection otherwise we would fix the current position
                        self.delete(self.position, tkinter.END)
                else: # set position to end so selection starts where textentry ended
                        self.position = len(self.get())
                # collect hits
                _hits = []
                for element in self._completion_list:
                        if element.lower().startswith(self.get().lower()):  # Match case-insensitively
                                _hits.append(element)
                # if we have a new hit list, keep this in mind
                if _hits != self._hits:
                        self._hit_index = 0
                        self._hits=_hits
                # only allow cycling if we are in a known hit list
                if _hits == self._hits and self._hits:
                        self._hit_index = (self._hit_index + delta) % len(self._hits)
                # now finally perform the auto completion
                if self._hits:
                        self.delete(0,tkinter.END)
                        self.insert(0,self._hits[self._hit_index])
                        self.select_range(self.position,tkinter.END)

        def handle_keyrelease(self, event):
                """event handler for the keyrelease event on this widget"""
                if event.keysym == "BackSpace":
                        self.delete(self.index(tkinter.INSERT), tkinter.END)
                        self.position = self.index(tkinter.END)
                if event.keysym == "Left":
                        if self.position < self.index(tkinter.END): # delete the selection
                                self.delete(self.position, tkinter.END)
                        else:
                                self.position = self.position-1 # delete one character
                                self.delete(self.position, tkinter.END)
                if event.keysym == "Right":
                        self.position = self.index(tkinter.END) # go to end (no selection)
                if event.keysym == "Down":
                        self.autocomplete(1) # cycle to next hit
                if event.keysym == "Up":
                        self.autocomplete(-1) # cycle to previous hit
                if len(event.keysym) == 1 or event.keysym in tkinter_umlauts:
                        self.autocomplete()

class AutocompleteCombobox(tkinter.ttk.Combobox):

        def set_completion_list(self, completion_list):
                """Use our completion list as our drop down selection menu, arrows move through menu."""
                self._completion_list = sorted(completion_list, key=str.lower) # Work with a sorted list
                self._hits = []
                self._hit_index = 0
                self.position = 0
                self.bind('<KeyRelease>', self.handle_keyrelease)
                self['values'] = self._completion_list  # Setup our popup menu

        def autocomplete(self, delta=0):
                """autocomplete the Combobox, delta may be 0/1/-1 to cycle through possible hits"""
                if delta: # need to delete selection otherwise we would fix the current position
                        self.delete(self.position, tkinter.END)
                else: # set position to end so selection starts where textentry ended
                        self.position = len(self.get())
                # collect hits
                _hits = []
                for element in self._completion_list:
                        if element.lower().startswith(self.get().lower()): # Match case insensitively
                                _hits.append(element)
                # if we have a new hit list, keep this in mind
                if _hits != self._hits:
                        self._hit_index = 0
                        self._hits=_hits
                # only allow cycling if we are in a known hit list
                if _hits == self._hits and self._hits:
                        self._hit_index = (self._hit_index + delta) % len(self._hits)
                # now finally perform the auto completion
                if self._hits:
                        self.delete(0,tkinter.END)
                        self.insert(0,self._hits[self._hit_index])
                        self.select_range(self.position,tkinter.END)

        def handle_keyrelease(self, event):
                """event handler for the keyrelease event on this widget"""
                if event.keysym == "BackSpace":
                        self.delete(self.index(tkinter.INSERT), tkinter.END)
                        self.position = self.index(tkinter.END)
                if event.keysym == "Left":
                        if self.position < self.index(tkinter.END): # delete the selection
                                self.delete(self.position, tkinter.END)
                        else:
                                self.position = self.position-1 # delete one character
                                self.delete(self.position, tkinter.END)
                if event.keysym == "Right":
                        self.position = self.index(tkinter.END) # go to end (no selection)
                if len(event.keysym) == 1:
                        self.autocomplete()
                # No need for up/down, we'll jump to the popup
                # list at the position of the autocompletion
def fonksiyon2():
        yazi2.config(text="Seçiminizi Yapınız",font="courier 20 bold")

def fonksiyon():
        x=combo.get()  


        yazi2.config(text = str(a) , font="courier 20 bold")
        
def test(test_list):
        root = tkinter.Tk()
        combo = AutocompleteCombobox(root)
        combo.set_completion_list(test_list)
        combo.pack()
        combo.focus_set()
        root.destroy()
     
import random
f = open("XMLCode.txt", errors='ignore')
A=[]
for line in f:         
        for word in line.split():         
                A.append(word)
B=[]
C=[]
D=[]
x=0
d=0
while x < len(A): #Comment
        if "alt=" in A[x]:
                if (A[x][5:-3:]) not in B:
                        B.append(A[x][5:-3:])
        x+=1
y=0
wordd=''
while y < len(A):     #Tags
        if "@" in A[y]:
                D.append(A[y])
                
        y+=1

g=0
j=0             
for i in D:
        g=0
        while g<len(i):
                if i[g]=='@':
                        if i[g+1:] not in C:
                                l=0
                                k=0
                                while k<len(i[g+1:]):
                                        if i[g+1:][k]=="<":
                                                C.append(i[g+1:g+1+l])
                                                break
                                        l+=1
                                        k+=1
                        
                                
                g+=1
                

E=[]
G=[]
for i in B:
        if i!='':
                E.append(i)
                G.append(i) #Sadece Yorum
for i in C:
        if i!='':
                E.append(i)        
Final=[]
for i in E:
        if not i in Final:
                Final.append(i)
Final1=[]
for i in G:
        if not i in Final1:   #Sadece Yorum List
                Final1.append(i)
                
finaltxt=open("List.txt","w")
S=1
for i in Final:
        finaltxt.write('%d' %S)
        finaltxt.write(" ) " + i + "\n")
        S+=1
finaltxt.close()
hh=len(Final)
final1txt=open("List.txt","w")
J=1
for i in Final1:   #Sadece Yorum
        final1txt.write('%d' %J)
        final1txt.write(" ) " + i + "\n")
        J+=1
final1txt.close()
hh1=len(Final1)


        
def CekilisFull():
        List=[]
        KazananListesi1=[]
        cc=random.randint(1,hh)
        if cc not in List:
                print("\n","Cikan Sayi : ",cc , "\n")
                print('Kazanan kisi  ' , Final[cc-1], "\n")
                a='Kazanan kisi:',Final[cc-1]
                KazananListesi1.append(Final[cc-1])
                List.append(cc)

        yazi2.config(text = a , font="courier 20 bold")
        
class cek():      
        def Cekilis():
                List=[]
                KazananListesi1=[]
                cc=random.randint(1,hh1)
                if cc not in List:
                        print("\n","Cikan Sayi : ",cc , "\n")
                        print('Kazanan kisi',Final1[cc-1], "\n")
                        a='Kazanan kisi:',Final1[cc-1]
                        KazananListesi1.append(Final1[cc-1])
                        List.append(cc)
                yazi2.config(text = a , font="courier 20 bold")
         


root = tkinter.Tk(className=' Çekiliş')
root.geometry("810x200+650+350")
yazi2=Label(root)
yazi2.config(text=" ",font="courier 20 bold")
yazi2.pack()          
yazi2=Label(root)
yazi2.config(text="Çekilişi Başlatmak için Seçiniz",font="courier 20 bold")
yazi2.pack()        
buton= Button(root)
buton.config(text = "Sadece Yorum Yapanlar Kişilerden", command = cek.Cekilis )
buton.pack()
buton3=Button(root)
buton3.config(text = "Yorum Yapan ve Etiketlenenlerden", command = CekilisFull)
buton3.pack()
root.mainloop()