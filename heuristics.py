from litcm import LIT
from guess_language import guess_language
import string
def printInputLang(hindiWords,tamilWords,englishWords):
		if (hindiWords !=0):
			inputLang = 'Transliterated Hindi'
			print 'Input language: ',inputLang
		elif (tamilWords !=0):
			inputLang = 'Transliterated Tamil'
			print 'Input language: ',inputLang
		elif (englishWords !=0):
			inputLang = 'English'
			print 'Input language: ',inputLang
lit = LIT(labels=['hin','eng','tam'],transliteration=True)
englishText = ['english','meaning','what','when','how','which']
tamilText = ['tamil','tamil script','artham','enna','epidi','eppo','entha']
hindiText = ['hindi','hindi script','arth','kya','kaun se','kaise','kab']
webQuery = raw_input("Enter search query :    ")
print webQuery
result = ''
query = webQuery.split()
result1 = any(i in tamilText for i in query)
if result1 == True:
	#print 'Based on the occurence of specific words in the query..'
	result = 'Tamil'
	print "Output language : ",result
result1 = any(i in hindiText for i in query)
if result1 == True:
	#print 'Based on the occurence of specific words in the query..'
	result = 'Hindi'
	print "Output language : ",result
result1 = any(i in englishText for i in query)
if result1 == True:
	#print 'Based on the occurence of specific words in the query..'
	result = 'English'
	print "Output language : ",result
lang = guess_language.guessLanguageName(webQuery)
if (lang!= 'UNKNOWN' and lang == 'Tamil'):
	inputLang = 'Tamil Script'
	print 'Input language: ',inputLang
	print "Output language :", lang
	#result = lang
#elif (lang =='UNKNOWN'):
	#if not result:
		#print 'Input language : Hindi '
		#print "Output language :", lang
else:
	if not result:
		langOutput = lit.identify(webQuery)
		print langOutput
		tamilWords = langOutput.count("Tam")
		englishWords = langOutput.count("Eng")
		hindiWords = langOutput.count("Hin")
		printInputLang(hindiWords,tamilWords,englishWords)
		'''print
		print 'Number of transliterated tamil words:  ',tamilWords
		print
		print 'Number of english words:  ',englishWords
		print
		print 'Number of transliterated hindi words:  ',hindiWords
		print
		print 'Based on the number of words in a given language..'
		print'''
		if (tamilWords>=englishWords and tamilWords>=hindiWords):
			print " Output language :Tamil  "
		elif (englishWords>=tamilWords and englishWords>=hindiWords):
			print " Output language :English  "
		elif (hindiWords>=englishWords and hindiWords>=tamilWords):
			print " Output language :Hindi  "
