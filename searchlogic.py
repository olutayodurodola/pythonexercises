#Search logic implemented
languages = ["Python", "Java", "C++", "C#", "JavaScript", "Go", "Rust", "C#", "Ruby", "Swift", "Kotlin", "PHP", "Perl", "C#",  "Scala", "Haskell", "Lua", "Dart", "Elixir", "Clojure", "F#", "R", "MATLAB", "Julia", "TypeScript", "Shell", "PowerShell", "Objective-C", "Visual Basic", "Assembly", "Fortran", "COBOL", "Ada", "Lisp"];


for i in range(5):
    if languages[i] == "Python":
        print(f"Language {i + 1}: {languages[i]} is the best programming language!");
    print(f"Language {i + 1}: {languages[i]}");

search_found_count = 0;
search_value = input("Enter a programming language to search for: ");
for language in languages:
    if language == search_value:
        print(f"{language} is found!");
        search_found_count += 1;
      #  break;
else:
    if search_found_count == 0:
        print(f"{search_value} is not found!");
print(f"Total found: {search_found_count}");