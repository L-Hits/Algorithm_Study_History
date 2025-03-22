n, B = map(int, input().split())

if n == 0:
  print("0")
else:
  digits = []
  while n:
    remainder = n % B
    if remainder < 10:
      digits.append(str(remainder))
    else:
      digits.append(chr(remainder + 55))
    n //= B

  print(''.join(digits[::-1]))
