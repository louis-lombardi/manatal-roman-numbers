def convert_roman(number):
    roman=''
    rom_digits = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    rom_digits_values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    digits_amount=13
    for i in range(digits_amount):   # apply succesive euclidian divisions to get the value of each digit weight, starting with M and finishing with I
        divisor = rom_digits_values[i]
        digits_to_add = number // divisor
        number = number % divisor
        roman = roman + digits_to_add * rom_digits[i]  # progressively add letters to the string 
    return(roman)

   
##### TEST #####     

i=int(input('Type a number : '))
print("The roman number is " + convert_roman(i))       