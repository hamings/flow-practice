Begin
    if n == 0 then
        return 0
    else if n == 1 then
        return 1
    else
        return fibonacci(N - 1) + fibonacci(N - 2)
    endif
End
