from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # O Django buscará automaticamente dentro da pasta templates/

    # criar dados mock de associado: ID, Nome, Status (ativo/Inativo)
    # criar um dicionario para representar o associado
    associados = [
    {'id': '001', 'nome': 'Romulo Jackson', 'status': 'Ativo'},
    {'id': '002', 'nome': 'David Quilan', 'status': 'Ativo'},
    {'id': '003', 'nome': 'Nayan Johnson', 'status': 'Inativo'},
    {'id': '004', 'nome': 'Cassio Dylan', 'status': 'Ativo'},
    {'id': '005', 'nome': 'Welligton Clinton', 'status': 'Inativo'},
    {'id': '006', 'nome': 'Marcos Jordan', 'status': 'Pendente'},
    {'id': '007', 'nome': 'Lucio Smith', 'status': 'Ativo'},
    {'id': '008', 'nome': 'Robert Brown', 'status': 'Ativo'},
    {'id': '009', 'nome': 'Mary Jackson', 'status': 'Inativo'},
    {'id': '010', 'nome': 'Enzo Smith', 'status': 'Pendente'},
    {'id': '011', 'nome': 'Wesley Cleriton', 'status': 'Ativo'},
    {'id': '012', 'nome': 'Denis Jonhson', 'status': 'Inativo'}
]
    return render(request,'associado/index.html', {'lista_associados': associados})
    #funcao para carregar o perfil do associado

def perfil(request):
    search = request.GET.get('search')
    # Se houver busca, filtra por nome ou status. Se não, traz tudo.
    if search:
        associados = Associado.objects.filter(
            models.Q(nome_completo__icontains=search) | 
            models.Q(status__icontains=search)
        )
    else:
        associados = Associado.objects.all()

    return render(request, 'associado/perfil.html', {'associados': associados})
def beneficios(request):
    # Por enquanto, apenas renderizamos o HTML de design
    return render(request, 'associado/beneficios.html')
def carteirinha(request):
    # Aqui passamos o contexto 'vibe pwa' para o template
    return render(request, 'associado/carteirinha.html')

