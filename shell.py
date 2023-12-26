import basic

text = input('basic > ')
if text.strip() == "": exit()
result, error = basic.run('<stdin>', text)
