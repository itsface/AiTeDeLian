from django.shortcuts import render


def api_comment_submit_test(request):
    return render(request, 'postTest.html')
