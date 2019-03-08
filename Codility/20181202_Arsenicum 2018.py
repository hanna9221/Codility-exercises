# Arsenicum 2018
# https://app.codility.com/cert/view/certPZ83ZM-272BWQVQBMMEYCPS/

def solution(s):
    words = s.split()
    words_reverse = []
    head, tail = [[] for i in range(26)], [[] for i in range(26)]
    for i in range(len(words)):
        if words[i] == words[i][::-1]: return words[i]
        words_reverse.append(words[i][::-1])
        head[ord(words[i][0])-97].append(i)
        tail[ord(words[i][-1])-97].append(i)
    
    def search(length, val, headList, tailList, record):
        if length > 600000: return None
        if val > 0: # search tail
            diff = headList[-1][record[-1][2]:]
            if diff==diff[::-1]:
                left = ' '.join(headList)
                right = ' '.join(tailList)
                return left + ' ' + right[::-1]
            target = ord(diff[0])-97
            for i in tail[target]:
                temp = words_reverse[i]
                lt = len(temp)
                if lt > val and diff==temp[:val]: 
                    new_val = val-lt
                    rec = (1, i, val)
                    if rec in record: return None
                    result = search(length+lt, new_val, headList,
                                    tailList+[temp], record+[rec])
                    if result: return result
                elif lt < val and diff[:lt]==temp:
                    new_val = val-lt
                    rec = (0, record[-1][1], record[-1][2]+lt)
                    if rec in record: return None
                    result = search(length+lt, new_val, headList,
                                    tailList+[temp], record+[rec])
                    if result: return result
                elif lt==val and diff==temp:
                    left = ' '.join(headList)
                    right = ' '.join(tailList+[temp])
                    return left + ' ' + right[::-1]
        else: # search head
            diff = tailList[-1][record[-1][2]:]
            if diff==diff[::-1]:
                left = ' '.join(headList)
                right = ' '.join(tailList)
                return left + ' ' + right[::-1]
            target = ord(diff[0])-97
            for i in head[target]:
                temp = words[i]
                lt = len(temp)
                if lt > -val and diff==temp[:-val]: 
                    new_val = val+lt
                    rec = (0, i, -val)
                    if rec in record: return None
                    result = search(length+lt, new_val, headList+[temp],
                                    tailList, record+[rec])
                    if result: return result
                elif lt < -val and diff[:lt]==temp: 
                    new_val = val+lt
                    rec = (1, record[-1][1], record[-1][2]+lt)
                    if rec in record: return None
                    result = search(length+lt, new_val, headList+[temp],
                                    tailList, record+[rec])
                    if result: return result
                elif lt==-val and diff==temp:
                    left = ' '.join(headList+[temp])
                    right = ' '.join(tailList)
                    return left + ' ' + right[::-1]
        return None
            
    for w in words:
        # rec=(0,0,0) --> head, words[0][0]
        # rec=(1,2,3) --> tail, words_reverse[2][3]
        result = search(len(w), len(w), [w], [], [(0,0,0)])
        if result: return result
    return 'NO'


#s = 'abc de fghijklkji hgfedcba'
#s = 'by metal owl egg mr crow worm my ate'
#s = 'abcc bc ac'
#s = 'ab cdab dcba'
s = 'abcde dcba'
print(solution(s))