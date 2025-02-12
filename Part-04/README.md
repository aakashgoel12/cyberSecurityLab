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

## Diagram Description
 
Imagine a simple diagram with two main components: the Client and the Server. Here's how you can visualize it:

1. Client Side:
    - A box labeled "Client" on the left side.
    - Inside the box, you can have the following steps:
         - Input Message: User types a message.
         - Encrypt Message: The message is encrypted using the encryption key.
         - Send Message: The encrypted message is sent to the server.
2. Server Side:
    - A box labeled "Server" on the right side.
    - Inside the box, you can have the following steps:
        - Receive Message: The server receives the encrypted message.
        - Decrypt Message: The server decrypts the message using the same encryption key.
        - Display Message: The server displays the decrypted message.
        - Input Response: Server user types a response.
        - Encrypt Response: The response is encrypted using the encryption key.
        - Send Response: The encrypted response is sent back to the client.
3. Arrows:
    - Draw arrows to show the flow of messages between the client and the server:
        - An arrow from "Send Message" in the Client box to "Receive Message" in the Server box.
        - An arrow from "Send Response" in the Server box to "Receive Response" in the Client box.

## Visual Representation
 
Here's a textual representation of the diagram:

```
+-------------------+                       +-------------------+  
|       Client      |                       |       Server      |  
|-------------------|                       |-------------------|  
| 1. Input Message  |                       |                   |  
| 2. Encrypt Message|                       |                   |  
| 3. Send Message   |  ------------------>  |  Receive Message  |  
|                   |                       |  Decrypt Message  |  
|                   |                       |  Display Message  |  
|                   |                       |  Input Response   |  
|                   |  <------------------  |  Encrypt Response |  
|                   |                       |  Send Response    |  
+-------------------+                       +-------------------+
```

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