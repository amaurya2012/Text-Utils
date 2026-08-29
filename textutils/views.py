from django.http import HttpResponse
from django.shortcuts import render


def playlist(request):
    return HttpResponse('<h1> Personal Navigator:- </h1>'
    '<h2> <a href = "https://youtu.be/JxzZxdht-XY?si=XFzUKKS2PepvsAcw"> Django CodeWithHarry Playlist </a> </h2>'
'<h2> <a href = "https://youtu.be/UrsmFxEIp5k?si=A1MSbBrTqslwkhpa"> Python CodeWithHarry Playlist </a> </h2>'
'<h2> <a href = "https://www.bing.com/ck/a?!&&p=b2e8e70657c592928da3040079aa380e14f8efc4ef2f84cefdeede24b7b82e77JmltdHM9MTc1ODA2NzIwMA&ptn=3&ver=2&hsh=4&fclid=3740589a-035a-6ee5-27f1-4ef3025c6f84&psq=quora&u=a1aHR0cHM6Ly93d3cucXVvcmEuY29tLw"> Quora Playlist </a> </h2>'
'<h2> <a href = "https://www.bing.com/ck/a?!&&p=4b68468044f963a9bef375b88040f7e0bf5cc1a5e5662244817b03c95e7f08d4JmltdHM9MTc1ODA2NzIwMA&ptn=3&ver=2&hsh=4&fclid=3740589a-035a-6ee5-27f1-4ef3025c6f84&psq=google+chrome&u=a1aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS9jaHJvbWUvaW5kZXguaHRtbA"> Google chrome </a> </h2>'
'<h2> <a href = "https://www.bing.com/ck/a?!&&p=34f97a7f24c69ec47d94ee57399a67e5eaa7c56926d2b62c9efb9eff0b76252cJmltdHM9MTc1ODA2NzIwMA&ptn=3&ver=2&hsh=4&fclid=3740589a-035a-6ee5-27f1-4ef3025c6f84&psq=copilot&u=a1aHR0cHM6Ly9jb3BpbG90Lm1pY3Jvc29mdC5jb20vP21zb2NraWQ9Mzc0MDU4OWEwMzVhNmVlNTI3ZjE0ZWYzMDI1YzZmODQ"> Copilot </a> </h2>')


def about(request):
    return HttpResponse("About Ajeyata")


# using template
def index(request):
    return render(request, 'index.html')


def analyze(request):
    # getting the text
    djtext = request.POST.get('text', 'default')

    # checking the checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    params = {}

    # check which checkbox is on
    if removepunc == "on":
        punctuationslist = ''':(){}[];''""\,<>-,/?@#$%!*_~`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuationslist:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):  # enumerate iterates the blank index spaces
            if not (djtext[index] == " " and index + 1 < len(djtext) and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extra Spaces Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = str(len(djtext))
        params = {'purpose': 'Char Count', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on"
            and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)