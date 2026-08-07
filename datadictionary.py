emails = { "caleb": "caleb@email.com",
           "tayo": "tayo@email.com" ,
           "john": "john@email.com",
            "tim": "tim@email.com",
             "james": "james@email.com",
              "obi":  ''}

print(f"Caleb's email address is: {emails['caleb']}");
print(f"Tayo's email address is: {emails['tayo']}");
print(f"John's email address is: {emails['john']}");
print(f"Tim's email address is: {emails['tim']}");
print(f"James's email address is: {emails['james']}");
print(f"Obi's email address is: {emails['obi']}");

for name, email in emails.items():
    print(f"{name.title()}'s email address is: {email}");


for i in emails:
    print(f"{i.title()}'s email address is: {emails[i]}");

for email in emails:
    print(email.title() + ": " + emails.get(email, "No email address found!"));

#Updating a value in the dictionary

emails["obi"] = "obi@email.com";
emails["josh"] = "josh@email.com";

emails.update({"amaka": "amaka@email.com"});

emails.update(ojo = "ojo@email.com", 
               chidi = "chidi@email.com");

print(emails);