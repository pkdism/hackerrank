regex_pattern = r"^(M{0,3})(CD|CM|D?C{0,3})(XL|XC|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

# Thousands : (M{0,3})
# Hundreds : (CD|CM|D?C{0,3})
# Tens : (XL|XC|L?X{0,3})
# Digits : (IX|IV|V?I{0,3})

import re
print(str(bool(re.match(regex_pattern, input()))))
