Analise o código abaixo:

```
while True:
	minute = get_minute()
	if minute is prime:
	    p = minute
	q = getPrime(1024)
	e = 65537
	n = p*q
	flag = "flag"
	c = pow(hex(flag), e, n)

	print(c, e, n)
```
