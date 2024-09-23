nums = {
    '1': 'bir',
    '2': 'ikki',
    '3': 'uch',
    '4': 'to`rt',
    '5': 'besh',
    '6': 'olti',
    '7': 'yetti',
    '8': 'sakkiz',
    '9': 'to`qqiz',
    '0': 'nol',
    '10': 'o`n',
    '20': 'yigirma',
    '30': 'o`ttiz',
    '40': 'qirq',
    '50': 'ellik',
    '60': 'oltmish',
    '70': 'yetmish',
    '80': 'sakson',
    '90': 'to`qson',
    '100': 'yuz'
}

def get_number_return_string(num: int) -> str:
    """ Function accept integer returned string """
    result = ""
    num_str = str(num)

    if len(num_str) == 3:
        yuzlik = num_str[0]
        if yuzlik in nums:
            result += nums[yuzlik] + " yuz "  # yuzlik xonani olish uchun
    num_str = num_str[1:]  # yuzlik xonani olib tashlash uchun ya`ni masalan: 121 => 21

    onlik = num_str[0] + "0"  # 2+0 = '20'
    birlik = num_str[1]

    if onlik in nums:
        result += nums[onlik]
        if birlik != 0 and birlik in nums:
            result += " " + nums[birlik]
    return result

   
if __name__ == "__main__":
    result = get_number_return_string(452)
    print(result)  # Output: to`rt yuz ellik ikki