# Flask-Sock example with communication between client and server

- The client strats a connection to the server
- The server echos the message back to the client
- The client prints the message
- The server maintains a thread posting time to the client every seconds
- The client prints the time
- The client can close the connection (message "close")
- The server close the connection when the client closes it
- The clock exits when the client closes the connection (exception followed by a break on the while loop)