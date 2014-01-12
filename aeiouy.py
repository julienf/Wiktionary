#! /usr/bin/python
# -*- coding: utf-8 -*-

import string

nomFich=raw_input("Filename?\n")
#nomFich="frwiktionary-20130718-all-titles-in-ns0-a"
#nomFich="frwiktionary-20121215-all-titles-in-ns0-a"
#nomFich="frwiktionary-20121215-all-titles-in-ns0-clean"
#nomFich="frwiktionary-20130718-all-titles-in-ns0-clean5"

def counting_vowels():
  file = open(nomFich, 'r')
  maxLen=0
  voyMax=0
  ligMax=0
  lineNb=0
  maxWord=""
  #print "pof"
  word1 = file.readline()
  word = word1.strip()
  while word:
    uWord = unicode(word, encoding='utf-8')
    lineNb+=1
    ligature=0
    voynb=0
    cur=0
    #print uWord
    for letter in uWord:
      oLetter=ord(letter)
      if(oLetter==65) or (oLetter==69) or (oLetter==73) or (oLetter==79) or (oLetter==85) or (oLetter==89):
	voynb+=1
      elif(oLetter==97) or (oLetter==101) or (oLetter==105) or (oLetter==111) or (oLetter==117) or (oLetter==121):
	#print "gah?"
	voynb+=1
      elif(oLetter>=192) and (oLetter<=197):
	voynb+=1
      elif(oLetter<=229) and (oLetter>=224):
	voynb+=1
      elif(oLetter>=256) and (oLetter<=261):
	voynb+=1
      elif(oLetter==461) or (oLetter==462):
	voynb+=1
      elif(oLetter==550) or (oLetter==551):
	voynb+=1
      elif(oLetter==230) or (oLetter==198):
	voynb+=1
	ligature+=1
      elif(oLetter>=200) and (oLetter<=203):
	voynb+=1
      elif(oLetter>=232) and (oLetter<=235):
	voynb+=1
      elif(oLetter>=274) and (oLetter<=283):
	voynb+=1
      elif(oLetter==400):
	voynb+=1
      elif(oLetter==552) or (oLetter==553):
	voynb+=1
      elif(oLetter>=296) and (oLetter<=305):
	voynb+=1
      elif(oLetter>=204) and (oLetter<=207):
	voynb+=1
      elif(oLetter>=236) and (oLetter<=239):
	voynb+=1
      elif(oLetter==463) or (oLetter==464):
	voynb+=1
      elif(oLetter==306) or (oLetter==307):
	voynb+=1
	ligature+=1
      elif(oLetter>=210) and (oLetter<=216):
	voynb+=1
      elif(oLetter>=242) and (oLetter<=248):
	voynb+=1
      elif(oLetter>=332) and (oLetter<=337):
	voynb+=1
      elif(oLetter==465) or (oLetter==466):
	voynb+=1
      elif(oLetter==338) or (oLetter==339):
	voynb+=1
	ligature+=1
      elif(oLetter>=554) and (oLetter<=561):
	voynb+=1
      elif(oLetter>=217) and (oLetter<=220):
	voynb+=1
      elif(oLetter>=249) and (oLetter<=252):
	voynb+=1
      elif(oLetter>=360) and (oLetter<=371):
	voynb+=1
      elif(oLetter>=467) and (oLetter<=476):
	voynb+=1
      elif(oLetter==374) or (oLetter==375) or (oLetter==376): #these are Y's
	voynb+=1
      elif(oLetter==221) or (oLetter==562) or (oLetter==563) or (oLetter==255) or (oLetter==253): #Y's also
	voynb+=1
      else:
	if(ligature>ligMax):
	  ligMax=ligature
	  #print "hep: "
	#if(voynb>=voyMax):
	if(voynb>=5):
	  voyMax=voynb
	  maxWord=word
	  print word, ";", voynb, ";", ligature
	ligature=0
	voynb=0
	
  
    word1 = file.readline()
    word = word1.strip()
  print voyMax, maxWord
  file.close()

def counting_consonants():
  file = open(nomFich, 'r')
  maxLen=0
  consMax=0
  maxWord=""
  word1 = file.readline()
  word = word1.strip()
  vowels=[65, 69, 73, 79, 85, 89, 97, 101, 105, 111, 117, 121, 192, 193, 194, 195, 196, 197, 198, 200, 201, 202, 203, 204, 205, 206, 207, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 224, 225, 226, 227, 228, 229, 230, 232, 233, 234, 235, 236, 237, 238, 239, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 255, 256, 257, 258, 259, 260, 261, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 332, 333, 334, 335, 336, 337, 338, 339, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 374, 375, 376, 400, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 491, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 603]
  while word:
    uWord = unicode(word, encoding='utf-8')
    consNb=0
    #print uWord
    for letter in uWord:
      oLetter=ord(letter)
      if(oLetter in vowels):
	if(consNb>=consMax):
	  consMax=consNb
	  maxWord=word
	  print word, ";", consNb
	consNb=0
      elif(oLetter in [45, 477, 596]): #- (dash), ǝ and ɔ. Are these last 2 vowels or consonants?
	if(consNb >=consMax):
	  consMax = consNb
	  maxWord = word
	  print word, ";", consNb
	consNb = 0
      else:
	consNb += 1
    word1 = file.readline()
    word = word1.strip()
  print consMax, "×", maxWord
  file.close()
  
def single_type():
  file = open(nomFich, 'r')
  maxLen=0
  typeMax=0
  maxWord=""
  word1 = file.readline()
  word = word1.strip()
  vowels=[65, 69, 73, 79, 85, 89, 97, 101, 105, 111, 117, 121, 192, 193, 194, 195, 196, 197, 198, 200, 201, 202, 203, 204, 205, 206, 207, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 224, 225, 226, 227, 228, 229, 230, 232, 233, 234, 235, 236, 237, 238, 239, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 255, 256, 257, 258, 259, 260, 261, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 332, 333, 334, 335, 336, 337, 338, 339, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 374, 375, 376, 400, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 491, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 603]
  while word:
    uWord = unicode(word, encoding='utf-8')
    typeNb=0
    for letter in uWord:
      oLetter=ord(letter)
      if(oLetter in vowels):
	typeNb+=1
	#print word, ";", typeNb
      elif(oLetter in [45, 477, 596]): #- (dash), ǝ and ɔ. Are these last 2 vowels or consonants?
	break
      else:
	break
    if((typeNb==len(word)) and (typeNb >= 4)):
      typeMax=typeNb
      print word, ";", typeNb
    word1 = file.readline()
    word = word1.strip()
  file.close()