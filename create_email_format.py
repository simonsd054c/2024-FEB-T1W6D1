# John Smith -> dairyfarm
# john.smith@dairyfarm.com.au

# first_name -> snake_case -> used for variables in python
# firstName -> camelCase -> used for variables in javascript
# FirstName -> PascalCase -> used for class names in almost all languages
# first-name -> kebab-case -> I don't know where it is used

# get first name of the person
first_name = input("What is your first name? ")

# get last name of the person
last_name = input("What is your last name? ")

# get the company name without space
company_name = input("What is your company name? Type it without spaces: ")

# create the email according to the format
predicted_email = f"{first_name}.{last_name}@{company_name}.com.au".lower()

# predicted_email = (first_name + "." + last_name + "@" + company_name + ".com.au").lower()

# display the email
print(predicted_email)