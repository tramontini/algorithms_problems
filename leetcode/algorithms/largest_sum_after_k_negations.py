# Para achar a maior soma, primeiro se negativa os menores valores.
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        # Ordenando a lista
        A.sort()

        i = 0

        # Inverte todos os menores que 0
        while K > 0 and i < len(A) and A[i] < 0:
            A[i] *= -1
            i += 1
            K -= 1

        # Se ainda tem inversões
        if K > 0:
            # Se esse valor for impar
            if K % 2 != 0:
                # Se não for primeira posição e o valor for maior que o anterior
                if i > 0 and A[i] > A[i-1]:
                    i -= 1

                A[i] *= -1



        return sum(A)


