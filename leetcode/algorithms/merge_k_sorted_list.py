
#https://leetcode.com/problems/merge-k-sorted-lists/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Cria a lista que vai receber os valores
        new_list = []
        # Para cada objeto singly-linked no na minha lista
        for i in lists:
            # Enquanto existir aquele objeto
            while i:
                # Adiciona o valor na lista nova
                new_list.append(i.val)
                # meu i atual vira minha proxima
                i = i.next

        # Orderna
        new_list.sort()

        # Retorna a lista
        # Contudo, talvez exista um erro no problema. Pois ele aceita o retorno da lista apenas e talvez devesse validar se é uma lista de objeto
        return new_list
