def num_to_words(number):
    ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'}
    teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'}
    tens = ['Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'}

    digits_in_number = len(number)
    a = number[-1]
    b = ((number % 10) - a)

    c = ((number % 100) - b)

    d = ((number % 1000) - c)
    e = ((number % 10000) - d)
    f = ((number % 100000) - e)

    g = ((number % 1000000) - f)
    h = ((number % 10000000) - g)
    i = ((number % 100000000) - h)

    j = ((number % 1000000000) - i)
    k = ((number % 10000000000) - j)
    l = ((number % 100000000000) - k)

    m = ((number % 1000000000000) - l)
    n = ((number % 10000000000000) - m)

    if digits_in_number == 0:
        return f"You did not provide a number"
    
    if digits_in_number == 1:
        return f"{ones[a]}"
    
    if digits_in_number == 2:
        if b == 1:
            return f"{teens[a]}"
        else:
            return f"{tens[b]} {ones[a]}"
    
    if digits_in_number == 3:
        if b == 1:
            return f"{ones[c]} Hundred and {teens[a]}"
        else:
            return f"{ones[c]} Hundred and {tens[b]} and {ones[a]}"

    if digits_in_number == 4:
        if b == 1:
            return f"{ones[c]} Hundred and {teens[a]}"
        else:
            return f"{ones[c]} Hundred and {tens[b]} and {ones[a]}"