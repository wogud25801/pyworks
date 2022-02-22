import re
# 주민번호 뒷 7자리 '*'로 마스킹

data = """
    kim 970610-1234567
    lee 950921-1234567
    han 020627-1234567 
"""

pat = re.compile("(\d{6})[-]\d{7}")
data2 = pat.sub("\g<1>-*******", data)
print(data2)