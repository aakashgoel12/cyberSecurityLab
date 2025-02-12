# Real-World Example: Encrypted Chat Application

## Prerequisites  
  
- Python: Make sure you have Python installed.
- Cryptography Library: Install the cryptography library using pip:
```
pip install cryptography
```

## How It Works
 
1. Server Initialization:
    - The server generates an encryption key and starts listening for incoming connections on port 5000.
    - When a client connects, the server sends the encryption key to the client.

2. Client Initialization:
    - The client connects to the server and receives the encryption key.
    - Both the client and server now have the same key for encryption and decryption.

3. Message Exchange:
    - The client prompts the user to enter a message, encrypts it using the shared key, and sends it to the server.
    - The server receives the encrypted message, decrypts it, and prints it.
    - The server then prompts the user to enter a response, encrypts it, and sends it back to the client.
    - The client receives the encrypted response, decrypts it, and prints it.

## Running the Example

1. Start the Server:
    - Run the server code in one terminal or command prompt window: python server_program.py  
 
2. Start the Client:
    - Run the client code in another terminal or command prompt window: python client_program.py  
 
3. Exchange Messages:
    - Enter messages in the client terminal to send them to the server.
    - Enter responses in the server terminal to send them back to the client.

## Summary

This example demonstrates a simple chat application where the client and server exchange encrypted messages. The encryption ensures that the messages are secure and cannot be read by unauthorized parties. This setup can be extended to more complex applications, such as secure messaging apps, online banking systems, and more.