"""  
Author: Aakash Goel  
Email: aakashgoel12@gmail.com  
"""
import socket  
from cryptography.fernet import Fernet  
  
def client_program():  
    # Create a new socket object  
    client_socket = socket.socket()  
      
    # Connect to the server running on the local host and port 5000  
    client_socket.connect(('localhost', 5000))
    print("Bound to localhost, port - 5000")
      
    # Receive the encryption key from the server  
    key = client_socket.recv(1024)
    print(f"Server key received to client : {key}")
    cipher_suite = Fernet(key)
      
    # Start an infinite loop to keep the client running  
    while True:  
        # Prompt the client user to enter a message to send  
        message = input("Enter message to send from client to server: ")  
          
        # Encrypt the message  
        encrypted_message = cipher_suite.encrypt(message.encode())  
        # Send the encrypted message to the server  
        client_socket.send(encrypted_message)  
        print(f"Encrypted Client Data sent to Server: {encrypted_message}")
          
        # Receive data from the server  
        data = client_socket.recv(1024).decode()  
        print(f"Encrypted Server Data received: {data}") 
        # Decrypt the received data and decode it to a string  
        decrypted_message = cipher_suite.decrypt(data.encode()).decode()  
        # Print the decrypted message received from the server
        print(f"Decrypted Server data: {decrypted_message}")
      
    # Close the connection  
    client_socket.close()  
  
if __name__ == "__main__":  
    client_program()  