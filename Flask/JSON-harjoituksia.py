#1)-----------------------------------------------------------------------------------
# Miten printtaat "key2"-kohdan valuen ?
import json
from textwrap import indent
json_one = """{"key1": "value1", "key2": "value2"}"""

#Expected output: "value2"

print(type(json_one))
data = json.loads(json_one)

#2)-----------------------------------------------------------------------------------
#Tutki https://docs.python.org/3/library/json.html, kohta pretty print.
#Printtaa seuraava JSON data, aseta parametrina indent level 2 ja separators (",", " = ").
json_two = {"key1": "value1", "key2": "value2"}
json_two["key3"]="value3"
# Expected Output:

# {
#   "key1" = "value2",
#   "key2" = "value2",
# }

prettier = json.dumps(json_two, indent=4, separators=(","," = "))
print(prettier)

#3)-----------------------------------------------------------------------------------
#Tallenna ja Sorttaa seuraava json aakkosjärjestykseen key:n mukaan. Aseta indent leveliksi 4: 
json_three = {"id" : 1, "name" : "value2", "age" : 29}
# Expected Output:

# {
#     "age": 29,
#     "id": 1,
#     "name": "value2"
# }

with open("json_three.json", "w") as f:
   json.dump(json_three,f, indent=4, sort_keys=True)

with open("json_three.json") as f:
   result = json.load(f)
   pretty= json.dumps(result, indent=4, separators=(",", " = "))
print(pretty)
#4)-------------------------------------------------------------------------------------
#Miten printtaat salaryn?

json_four = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
# Expected output: 7000
data = json.loads(json_four)
print(data['company']['employee']['payble']['salary'])

#5)------------------------------------------------------------------------------------
#https://docs.python.org/3/library/json.html
#Tutki em. dokumentaatiosta, miten command linesta voi ajaa JSON-validaattoria, esim. seuraavassa:
#Validaattorin tulee kertoa "Expecting ',' delimiter..." eli kertoa pilkun puuttuminen.

# { 
#     "company":{ 
#        "employee":{ 
#           "name":"emma",
#           "payble":{ 
#              "salary":7000
#              "bonus":800
#           }
#        }
#     }
#  }