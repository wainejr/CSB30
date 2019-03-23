# Código

#### Considerações gerais

- Todo código, comentário e nome de arquivo deve ser escrito em inglês
- Sempre iniciar comentários com letras maiúsculas
- Utilizar aspa única tanto para variáveis quanto para comentários em bloco (e.g. ``var = 'weight'``, ``''' My comment '''``)
- Para arquivos modulares, sempre deve haver no início do arquivo uma breve descrição do seu conteúdo
- Definir a parte do código que irá rodar dentro de ``if (__name__ == '__main__'):``

#### Variáveis

- Utilizar nomes significativos
- Underline para separação entre palavras
- Primeira letra sempre minúscula

#### Funções

- Utilizar underline para separação entre palavras
- Comentar funções com descrição do seu funcionamento, quando julgar necessário, e seus parâmetros, se esses não forem autodescritivos

#### Classes

- Classes devem sempre começar com letra maiúscula
- Utilizar letras maiúsculas para separar palavras
- A função ``__init__()`` deve sempre ser a primeira a ser declarada na classe

#### Constantes

- Devem ser escritas com todas letras maiúsculas
- Underline para separação entre palavras

#### Organização do código

- Devem ser definidos respectivamente: os imports, as constantes, as classes, as funções e a ``main()``.

#### Exemplo de código
    
    '''
        My module description
    '''

    import someModule

    MY_CONSTANT_STRING = 'vaTapaueR'

    class MyClass:
    ''' My class description '''
        def __init__(self, name)
            self.name = name

        def is_John():
            if(self.name == 'John'):
                return (True)
            return (False)


    def my_function(num1, num2):
        ''' Returns the sum of the args plus 42 '''
        my_number = 42
        return (num1 + num2 + my_number)


    if(__name__ = '__main__'):
        number1 = 100
        number2 = 654

        print(my_function(number1, number2))

# GIT

#### Considerações gerais

- Sempre realizar um pull antes de começar a alterar os arquivos, assim como antes de dar commit/push
- Não adicionar arquivos de tamanho grande, como vídeos

#### Branches

- Para cada ramo do trabalho deve ser criada uma branch. Para tarefas mais rápidas, pode-se utilizar a branch _working_ para modificação do código.
- O código só deve ser mergido com a branch _master_ quando estiver livre de bugs não necessitar de demais alterações
- Branches que forem dependentes devem ser mergidas entre si para testes e só depois mergidas para a _master_


#### Commits

- Os commits devem sempre conter mensagens em inglês com uma breve descrição do que foi feito
- Deve-se evitar adicionar arquivos temporários

# Documentação

#### Considerações gerais

- Bugs não arrumados, classes não finalizadas e demais tarefas a fazer devem ser adicionadas ao arquivo TODO.md 
- Cada tipo de diagrama deve possuir uma pasta só para si
- Deve ser utilizado o mesmo formato de arquivo de modelagem para todos diagramas.
- Sempre salvar os diagramas também em formato de imagem (png) ou em PDF, após suas alterações
- Os modelos devem estar atualizados com o código e vice-versa. Caso não estejam, deve ser explicitado que não estão e adicionada a tarefa de atualização ao TODO.md