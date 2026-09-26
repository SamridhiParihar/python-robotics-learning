# create  variables containig : integer, float , boolean , string , 
# complex number  and print it's type and value 

var1: int = 10
var2: float = 20.34
var3: bool = True 
var4: str = "Samridhi Parihar"
var5: None = None
var6: complex = 3 + 4j


variables = {
    "var1": var1,
    "var2": var2,
    "var3": var3,
    "var4": var4,
    "var5": var5,
    "var6": var6
}

for name, value in variables.items():
    print(f"{name} type is: {type(value)}")



# string analyzer : take a sentence from the user and print 
# original sentence , no of chars , first char , last char , upper case
# lower case version 

usr_var: str = input("enter the sentence pls ")
print(f"No of chars: {len(usr_var)}\nFirst char is: {usr_var[0]}\nLast char is: {usr_var[len(usr_var)-1]}\nUpper case version of it is: {usr_var.upper()}\nLower case version of it is: {usr_var.lower()}")

#username processor : remove whitespace , convert it to lowercase , print processed user name , print len

usr_name: str = input("enter the username pls ")
crct_usr_name: str = usr_name.strip().lower()

print(f"username: {crct_usr_name}\nlength: {len(crct_usr_name)}")

# email analyzer : take email address and split username and domain 
usr_email: str = input("enter the correct email address ")
usr_name_domain: list = usr_email.split("@")
print(f"Username: {usr_name_domain[0]}\nDomain: {usr_name_domain[1]}")


#reverse text 
txt: str = input("enter the text pls ")
reversed_txt = txt[::-1]
print(f"Original: {txt}\nReversed: {reversed_txt}")


#palindrome 
def is_palindrome(txt: str) -> bool :
    cor_txt = txt.replace(" ", "").lower()
    n: int = len(cor_txt)
    for i in range (n//2):
        if cor_txt[i]!=cor_txt[n-i-1]:
            return False
    return True

txt_pal: str = input("enter the text ")
print(f"The given text is palindrome or not : {is_palindrome(txt_pal)}")

# word counter (only limited to spaces) and print on separate line
sen: str = input("enter the sentence")
sen_list: list[str] = sen.split()
print(f"No of words are: {len(sen_list)}")
for value in sen_list:
    print(value)