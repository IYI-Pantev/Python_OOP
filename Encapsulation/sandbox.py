import re

email = "pe77er@gmail.com"

(name, mail, domain) = re.split('[@.]', email)

print(name, mail, domain)