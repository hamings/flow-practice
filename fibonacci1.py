Begin
    if n == 0 then
        return 0
    else if n == 1 then
        return 1
    else
        return fibonacci(N - 1) + fibonacci(N - 2)
    endif
End

if __name__ == '__main__':
    N = 7
    print(f"{N}th Fibonacci term is:", fibonacci(N))
