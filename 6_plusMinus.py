'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

Example: arr = [1,1,0,-1,-1]

There are n=5 elements, two positive, two negative and one zero. Their ratios are 2/5=0.400000, 2/5=0.400000 and 1/5=0.200000. Results are printed as:

0.400000
0.400000
0.200000
Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers

Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with 6 digits after the decimal. The function should not return a value.

Input Format

The first line contains an integer, n, the size of the array.
The second line contains n space-separated integers that describe arr[n].
'''
arr= [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    resultado = []
    positivos = 0
    negativos = 0
    ceros = 0
    
    
    for i in range(len(arr)):
        ratios =0
        #print(arr[i])
        
        if arr[i] > 0:
            positivos += 1
        elif arr[i] < 0:
            negativos += 1
        else:
            ceros += 1
    print('positivos: ', positivos, '\nNegativos: ', negativos, "\nCeros: ", ceros)
    
    #print('es positivo')
    ratiosP = "{:.6f}".format(positivos/n)
    resultado.append(ratiosP)
    ratiosN = "{:.6f}".format(negativos/n)
    resultado.append(ratiosN)
    ratiosC = "{:.6f}".format(ceros/n)
    resultado.append(ratiosC)
    #print(resultado)
            
    for datos in resultado:
        print(10*'-')
        print(datos)
    
plusMinus(arr)