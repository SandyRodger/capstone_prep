def greet(language_code):
    match language_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

def extract_language(locale):
  return locale[0:2]

def extract_region(locale):
  return locale[3:5]

def local_greet(locale):
  lang = extract_language(locale)
  reg = extract_region(locale)
  greet = local_greet(locale)

  match reg:
    case 'US':
      return 'Hey!'
    case 'GB':
      return 'Hello!'
    case 'AU':
      return 'Howdy!'
  
case 'fr':
    return 'Salut!'

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!