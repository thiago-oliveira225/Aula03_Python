

def is_palindrome(n):
    # Função para verificar se um número é um palíndromo
    return str(n) == str(n)[::-1]

def find_largest_palindrome():
    largest_palindrome = 0

    for num1 in range(1000, 10000):
        for num2 in range(1000, 10000):
            product = num1 * num2
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome

result = find_largest_palindrome()
print("O maior palíndromo é:", result)





