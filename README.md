## login-microservice

This microservice was written by rifflee

The program will continuously read from createRequest.txt and loginRequest.txt.

When a login request is received, it will be checked against the users.txt file.

If there is a matching username and password, it will return authenticated: True.

Otherwise it will return authenticated: False.

When a create request is received, the username and password will be written to
the user.txt file.
