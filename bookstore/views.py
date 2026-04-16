import git
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def update(request):
    if request.method == "POST":
        try:
            repo = git.Repo('/home/Handerrr/bookstore')
            origin = repo.remotes.origin
            origin.pull()
            return HttpResponse("Updated code on PythonAnywhere")
        except Exception as e:
            return HttpResponse(f"Erro: {str(e)}")
    else:
        return HttpResponse("Método inválido")