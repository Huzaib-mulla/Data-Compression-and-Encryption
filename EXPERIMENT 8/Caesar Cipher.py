import pyperclip
def main():
  myMessage = 'CEASER CIPHER DEMO'
  myKey = 3
  ciphertext = encryptMessage(myKey, myMessage)
   
  print("Cipher Text is")
  print(ciphertext + '|')
  pyperclip.copy(ciphertext)

def encryptMessage(key, message):
  ciphertext = [''] * key
   
  for col in range(key):
    position = col
    while position < len(message):
      ciphertext[col] += message[position]
      position+=key
  return ''.join(ciphertext) #Cipher text

if __name__ == '__main__':
  main()