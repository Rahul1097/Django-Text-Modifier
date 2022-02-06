from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyze(request):

    #get text
    djtext = request.POST.get('text','default')
    params = {}
    purpose = ''

    #check if checkboxes value is on
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    lowercaps = request.POST.get('lowercaps','off')
    capitalize = request.POST.get('capitalize','off')
    title = request.POST.get('title','off')
    trim = request.POST.get('trim','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount','off')
    wordcount = request.POST.get('wordcount','off')

    if removepunc == 'on':
        punctuations ='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed= ''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        purpose = 'Removed Punctuations'
        params = {'purpose':purpose,'analyzed_text':analyzed}
        djtext = analyzed
   
    if fullcaps =='on':
        analyzed =''
        for char in djtext:
            analyzed += char.upper()
        if purpose != '':
            purpose += ', ' + 'Changed to UpperCase'
        else:
            purpose = 'Changed to UpperCase'
        params = {'purpose':purpose,'analyzed_text':analyzed}
        djtext = analyzed

    if lowercaps =='on':
        analyzed =''
        for char in djtext:
            analyzed += char.lower()
        if purpose != '':
            purpose += ', ' + 'Changed to LowerCase'
        else:
            purpose = 'Changed to LowerCase'
        params = {'purpose':purpose,'analyzed_text':analyzed}
        djtext = analyzed

    if capitalize =='on':
        analyzed = djtext.capitalize()
        if purpose != '':
            purpose += ', ' + 'Capitalized the string'
        else:
            purpose = 'Capitalized the string'
        params = {'purpose':purpose,'analyzed_text':analyzed}
        djtext = analyzed

    if title =='on':
        analyzed = djtext.title()
        if purpose != '':
            purpose += ', ' + 'Displayed as Title'
        else:
            purpose = 'Displayed as Title'
        params = {'purpose':purpose,'analyzed_text':analyzed}
        djtext = analyzed

    if trim =='on':
        analyzed = djtext.strip()
        if purpose != '':
            purpose += ', ' + 'Timmed spaces'
        else:
            purpose = 'Timmed spaces'
        params = {'purpose':purpose,'analyzed_text':analyzed}
        djtext = analyzed

    if newlineremover =='on':
        analyzed =''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        if purpose != '':
            purpose += ', ' + 'Removed new lines'
        else:
            purpose = 'Removed new lines'
        params = {'purpose':purpose,'analyzed_text':analyzed}
        djtext = analyzed

    if spaceremover =='on':
        analyzed =''
        for index,char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index+1] ==' ':
                pass
            else:
                analyzed += char
        if purpose != '':
            purpose += ', ' + 'Removed extra spaces'
        else:
            purpose = 'Removed extra spaces'
        params = {'purpose':purpose,'analyzed_text':analyzed}
        djtext = analyzed
        
    if charcount =='on':
        count = 0
        for char in enumerate(djtext):
            count +=1
        if purpose != '':
            purpose += ", " + 'Character Count'
            analyzed += "\n" + "Total no of characters - " + str(count)
        else:
            purpose = 'Character Count'
            analyzed = "Total no of characters - " + str(count)
        params = {'purpose':purpose,'analyzed_text':analyzed}

    if wordcount =='on':
        count = 0
        for word in djtext.split():
            count += 1
        if purpose != '':
            purpose += ", " + 'Word Count'
            analyzed += "\n" + "Total no of words - " + str(count)
        else:
            purpose = 'Word Count'
            analyzed = "Total no of words - " + str(count)
        params = {'purpose':purpose,'analyzed_text':analyzed}
        djtext = analyzed

    if (removepunc != 'on' and fullcaps !='on' and lowercaps !='on' and capitalize != 'on' and title != 'on' and trim != 'on' and newlineremover !='on' and spaceremover !='on' and  charcount !='on' and wordcount != 'on'):
        return HttpResponse("Error! Please select any operation and try again.")

    return render(request,"analyze.html",params)