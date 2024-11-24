from django.shortcuts import render

from django.http import HttpResponse
def shannu(request):
    return HttpResponse('shannu is a innocent boy')


def pradeep(request):
    return HttpResponse('<h1>he is very smart and kind</h1>')
 
def madhuri(request):
    return HttpResponse('<h1><marquee>she is very hardworker and kind</marquee></h1>')

def masthanaiah(request):
    return HttpResponse('''
                        <h1>he is good human being</h1>
                        <b>he give more love towards lovely daughters</b><br>
                        <i>he is stylish</i>
                        <img src="https://tse2.mm.bing.net/th?id=OIP.NSVOuXn688OKU8ckpCrSygHaL2&pid=Api&P=0&h=180" alt="">
                        ''')
