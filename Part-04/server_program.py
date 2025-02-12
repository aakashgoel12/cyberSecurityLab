"""  
Author: Aakash Goel  
Email: aakashgoel12@gmail.com  
"""
import socket  
from cryptography.fernet import Fernet  
  
# Generate a key for encryption and decryption  
# You must use the same key for both client and server  
key = Fernet.generate_key()  
cipher_suite = Fernet(key)  
  
def server_program():  
    # Create a new socket object  
    server_socket = socket.socket()
      
    # Bind the socket to the local host and port 5000  
    server_socket.bind(('localhost', 5000))
    print("Bound to localhost, port - 5000")
      
    # Listen for incoming connections  
    server_socket.listen(1)
    print("Server is listening on port 5000...")
    
    # Accept a connection from a client  
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))  
      
    # Send the encryption key to the client  
    conn.send(key)  
    print(f"Key sent to client - {key}")
    # Start an infinite loop to keep the server running  
    while True:  
        # Receive data from the client  
        data = conn.recv(1024).decode()  
        print(f"Encrypted Client Data received: {data}")
        # If no data is received, break the loop  
        if not data:  
            break  
          
        # Decrypt the received data and decode it to a string  
        decrypted_message = cipher_suite.decrypt(data.encode()).decode()  
        print(f"Decrypted client data: {decrypted_message}")  
        
        # Prompt the server user to enter a message to send  
        message = input("Enter message to send from server to client: ")  
        
        # Encrypt the message  
        encrypted_message = cipher_suite.encrypt(message.encode())
        # Send the encrypted message to the client  
        conn.send(encrypted_message)
        print(f"Encrypted Server Data sent to client: {encrypted_message}")

    # Close the connection  
    conn.close()  
  
if __name__ == "__main__":  
    server_program()  