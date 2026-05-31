# Solution: Even or Odd
def even_or_odd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"

# Solution: Reversed Strings
def solution(string):
    return string[::-1]

print(solution('world'))

# Solution: Goldbach's Conjecture
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True
    
    
def goldbach(even_number):
    pairs = []
     
    for num in range(2, even_number // 2 + 1):
        other = even_number - num
        
        if is_prime(num) and is_prime(other):
            pairs.append([num, other])
            
            
            
    return pairs

# Solution: Vowel Count 

def get_count(sentence):
    count = 0
    for char in sentence:
        if char in 'aeiou':
            count += 1
    return count