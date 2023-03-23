str = 'X-DSPAM-Confidence:0.8475'
num = str.find(':')
nums = str[num + 1 :]
x = float(nums)
print(x)

