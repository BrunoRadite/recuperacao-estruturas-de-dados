class Questa2:
    
    @staticmethod
    def backspaceReturn(s,t):
        #pilha principal do parametro s
        pilhaS =[]
        
        #pilha principal do parametro t
        pilhaT =[]
        
        #pilhas para guardar os elementos das pilhas principais 
        pilhaReservaS =[]
        pilhaReservaT =[]
        
        #quantidade de backspaces seguidos
        backS = 0
        backT = 0
        
        #alimentando as pilhas s e t com o valor das strings parametro s e t
        for i in s:
            pilhaS.append(i)
        
        for i in t:
            pilhaT.append(i)
        
        #vamos rodar atraves da pilhaS
        while len(pilhaS) >0:
            
            #rodar um for reverso para termos sempre o topo da pilha
            for i in pilhaS.__reversed__():
                
                #vamos verificar se o valor é um backspace caso seja vamos adicionar + 1 no numero de backspaces seguidos
                #depois vamos tirar esse caractere da nossa lista
                if i == "#":
                    backS +=1
                    pilhaS.pop()
                    
                #vamos verificar se esse elemento que é diferente de # vem depois de um #
                elif backS > 0 and i != '#' :
                    
                    #se vinher vamos tirar a quantidade de # seguidos da lista
                    for _ in range(backS):
                        pilhaS.pop()
                        
                        #caso não tenha mais como fazer o pop() ele para o for
                        if(len(pilhaS)==0):
                            break
                        
                    #limpando o back pois o proximo que vinher não será seguido
                    backS = 0
                
                #se o elemento não foi apagado ele entra na lista reserva 
                else:
                    pilhaReservaS.append(i)
                    pilhaS.pop()
               
        #vamos voltar os elementos para a lista principal para eles ficarem na ordem correta      
        for i in pilhaReservaS.__reversed__():
            pilhaS.append(i)
        
        #limpando a lista reserva
        pilhaReservaS.clear()
        
        #vamos rodar atraves da pilhaT
        while len(pilhaT) >0:
            
            #rodar um for reverso para termos sempre o topo da pilha
            for i in pilhaT.__reversed__():
                
                #vamos verificar se o valor é um backspace caso seja vamos adicionar + 1 no numero de backspaces seguidos
                #depois vamos tirar esse caractere da nossa lista
                if i == "#":
                    backT +=1
                    pilhaT.pop()
                    
                #vamos verificar se esse elemento que é diferente de # vem depois de um #
                elif backT > 0 and i != '#' :
                    
                    #se vinher vamos tirar a quantidade de # seguidos da lista
                    for _ in range(backT):
                        pilhaT.pop()
                        
                        #caso não tenha mais como fazer o pop() ele para o for
                        if(len(pilhaT)==0):
                            break
                        
                    #limpando o back pois o proximo que vinher não será seguido
                    backT = 0
                
                #se o elemento não foi apagado ele entra na lista reserva     
                else:
                    pilhaReservaT.append(i)
                    pilhaT.pop()
                
        #vamos voltar os elementos para a lista principal para eles ficarem na ordem correta          
        for i in pilhaReservaT.__reversed__():
            pilhaT.append(i)
        
        #limpando a lista reserva
        pilhaReservaT.clear()
         
        #verificando se as pilhas são iguais se sim retorna true 
        if(pilhaS == pilhaT):
            print(True)
            return True
          
        #se não false  
        else:
            print(False)
            return False
