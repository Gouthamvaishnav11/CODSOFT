import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','0']


def generate_password(length):
      # Define the characters to use in the password
      characters =letters+numbers

      # Generate a random password
      password = ''.join(random.choice(characters) for _ in range(length))

      return password

def main():
      # Prompt the user to specify the desired length of the password
      try:
          length = int(input("Enter the desired length of the password: "))
          if length < 1:
              raise ValueError("Password length must be at least 1.")
      except ValueError as ve:
          print(f"Invalid input: {ve}")
          return

      
      password = generate_password(length)
    

      # Display the generated password
      print("Generated password:", password) 

if __name__ == "__main__":
      main()

