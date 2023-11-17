def plusOne(digits):
    last = len(digits) - 1

    if digits[last] != 9: # se o ultimo for diferente de 9, apenas acrescenta
        digits[last] += 1
        return digits

    for i in range(len(digits) - 1, 0, -1): 
        if digits[i] == 9 and digits[i - 1] == 9:
            # vou trocando todos os 9 para 0, até achar um número diferente de 9
            digits[i] = 0

        if digits[i] == 9 and digits[i - 1] != 9:
            # [1, 2, 9] -> se o atual for 9 e o próximo no loop for diferente de nove, atribui 0 ao atual e incrementa um ao próximo
            digits[i] = 0
            digits[i - 1] += 1
            return digits

    # caso saia do loop com todos os 9 trocados para zero, acrescentamos 1 ao inicio do array
    if digits[0] == 9:
        digits[0] = 0
        digits.insert(0, 1)

    return digits


def matchingStrings(strings, queries): # O(n)
    mapping = {}
    for i in range(len(strings)):
        if strings[i] not in mapping:
            mapping[f'{strings[i]}'] = 1
        else:
            mapping[f'{strings[i]}'] += 1
    
    controller = []
    for j in range(len(queries)):

        if queries[j] in mapping:
            controller.append(mapping[queries[j]])
        else:
            controller.append(0)
        
    return controller

def pangrams(s):
    range_list = list(s) # interaçoes
    str_sample = s.lower() # minusculas para definir cada letra
    arr = [0] * 26 # alfabeto

    for i in range(len(range_list)):
        each_letter = ord(str_sample[i]) - ord('a') # da a posição e cada letra no alfabeto
        
        if each_letter >= 0:
            arr[each_letter] += 1 # se for maior que 0 adicionamos 1 a posicao daquela letra

    for j in arr:
        if j == 0:
            return 'not pangram'
    
    return 'pangram'
