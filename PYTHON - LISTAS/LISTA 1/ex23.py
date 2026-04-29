"""
Considere o código a seguir:
n = 6 
i = 0
while i < n:
    if i % 2 == 0:
        n = n - 1
    i += 1
print(i, n)
Determine os valores finais de i e n e explique como a modificação dinâmica de n
influencia o número de iterações do loop.
"""

n = 6 
i = 0
while i < n:
    if i % 2 == 0:
        n = n - 1
    i += 1
print(i, n)