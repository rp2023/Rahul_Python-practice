#Defining configuration variable for a web server
server_name="my_server"
port =80
is_https_enabled=True
max_connection=1000

#print the configuration
print(f"server Name:", server_name)
print(f"Port:", port)
print(f"HTTPS enabled:", is_https_enabled)
print(f"Max connection:", max_connection)

#update configuration value

port=443
is_https_enabled=False

#print the updated configuration
print(f"Updated port:", port)
print(f"Updated HTTPS enabled:", is_https_enabled)

#In this example, we use variables to store and manipulate configuration data for a web server.
# This allows us to easily update and manage the server's configuration in a DevOps context.