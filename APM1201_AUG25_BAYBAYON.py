def numtowords(num):
    ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
    teens = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    words = ''
    if num <= 10:
        words += ones[num]
        return words
    elif num < 20:
        words += teens[num - 11]
        return words
    elif num < 100:
        words += tens[num // 10 - 2]
        if num % 10 != 0:
            words += ('-' + numtowords(num % 10))
        return words
    elif num < 1000:
        words += (ones[num // 100] + ' Hundred')
        if num % 100 != 0:
            words += (' ' + numtowords(num % 100))
        return words
    elif num < 10000:
        words += (ones[num // 1000] + ' Thousand ') 
        if num % 1000 != 0:
            words += (numtowords(num % 1000))     
        return words
    
    else:
        return 'Ten Thousand'

while True:
    num = int(input("Enter a number (0-10000): "))
    if num >= 0 and num <= 10000:
        word_form = numtowords(num)
        print(f"Words: {word_form}")
        break
    else:
        print("Please enter a number from 0 to 10000 only!")

end = input("Exit: ")