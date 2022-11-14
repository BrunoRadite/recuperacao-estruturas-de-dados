class minPilha:
    
    def __init__(self):
        self.__pilha = []


    #metodo de apagar o topo da pilha
    def pop(self):
        
        #verificando se a pilha possui elementos
        if len(self.__pilha) > 0:
            self.__pilha.pop()
        
        #caso não tenha ele retornará None e mostrará no terminal o que ocorreu
        else:
            print('A pilha não possui nenhum elemento')
            return None
    
    
    #metodo para adicionar um elemento no final da pilha
    def push(self, elemento):
        self.__pilha.append(elemento)
    
    
    #metodo que irá retorna o topo da lista
    def top(self):
        #verificando se a pilha possui elementos
        if len(self.__pilha) > 0:
            #retornando o ultimo elemento da lista que é o topo da pilha
            print(self.__pilha[-1])
            return self.__pilha[-1]
        
        #caso não tenha ele retornará None e mostrará no terminal o que ocorreu
        else:
            print('A pilha não possui nenhum elemento')
            return None
    
    
    def getMin(self):
        #verificando se a pilha possui elementos
        if len(self.__pilha) > 0:
            #criando a variavel min que por padrão terá o topo da lista
            min = self.top()
            
            #revertendo o for para ir do topo até o primeiro
            for i in self.__pilha.__reversed__():
                
                #verificando cada elemento para ver se é menor que o ultimo min, se for atualiza o min
                if str(i) < str(min):
                    min = i      
                    
            #depois de tudo verificado  retorna o min
            print(min)
            return min
        
        #caso não tenha ele retornará None e mostrará no terminal o que ocorreu
        else:
            print('A pilha não possui nenhum elemento')
            return None

