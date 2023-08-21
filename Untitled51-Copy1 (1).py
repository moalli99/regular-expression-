#rugular expression
# 

# In[13]:


import re
my_file=open("new.txt","r")
content_file=my_file.read()
name_list=[]
phoneNumber_list=[]
emails_list=[]

pattern=re.compile("[A-Z]+[a-z]+\s[A-z]+[a-z]+\s")
matches=pattern.finditer(content_file)
for match in matches:
    start=match.span()[0]
    end=match.span()[1]
    name_list.append(content_file[start:end])
pattern=re.compile(r"010\d{7}")
matches=pattern.finditer(content_file)
for match in matches:
    start=match.span()[0]
    end=match.span()[1]
    phoneNumber_list.append(content_file[start:end]) 
pattern=re.compile(r"012\d{7}")
matches=pattern.finditer(content_file)
for match in matches:
    start=match.span()[0]
    end=match.span()[1]
    phoneNumber_list.append(content_file[start:end]) 
pattern=re.compile(r"[A-z]+@[a-z]+\.[c|n|e]\w+")
matches=pattern.finditer(content_file)
for match in matches:
    start=match.span()[0]
    end=match.span()[1]
    emails_list.append(content_file[start:end])     
print(name_list)    
print(phoneNumber_list)
print(emails_list)


# In[ ]:




