letter = "helloooooo itzz {1} and i'm from {0}"
country = "India"
name = "luka"

print(letter.format(country,name))
print(letter.format(name,country))
# the order issue can be    removed by using string
# can simply plugin values in string simplty use fstrings

print(f"heyyyyy this is {name} and i'm from {country}")
#  if you've to show {} in your strings while iusing fstrings : use double {{ }}
# one will be retrained  
price = 86.729
text = f"For only {price: .2f} dollars!"
print(text)
