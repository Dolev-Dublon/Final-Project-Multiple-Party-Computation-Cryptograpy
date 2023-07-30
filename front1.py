import socket
import json
from unionA import union
HOST,PORT = '127.0.0.1',8080
 
my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
my_socket.bind((HOST,PORT))
my_socket.listen(1)
 
print('Serving on port ',PORT)

def process_data(data):
    # this function is where you will perform the calculations on the list of numbers
    # I'll use a dummy function that simply returns the numbers squared
    return [num**2 for num in data]
 
while True:
    connection,address = my_socket.accept()
    request = connection.recv(50240).decode('utf-8')
    string_list = request.split(' ')     # Split request from spaces
 
    method = string_list[0]
    requesting_file = string_list[1]
 
    print('Client request ',requesting_file)
    if method == 'POST':
        # Extract the JSON body of the request
        body = request.split('\r\n\r\n')[1]
        data = json.loads(body)
        print(data)

        # Perform the calculation
        result = union(data,16)
        print(result)

        # Send a JSON response
        response = json.dumps(result)
        header = 'HTTP/1.1 200 OK\n'
        mimetype = 'application/json'
        header += 'Content-Type: '+str(mimetype)+'\n\n'
        final_response = header.encode('utf-8')
        final_response += response.encode('utf-8')
        connection.send(final_response)
        connection.close()
    else:
        myfile = requesting_file.split('?')[0] # After the "?" symbol not relevent here
        myfile = myfile.lstrip('/')
        if(myfile == ''):
            myfile = 'index1.html'    # Load index file as default
    
        try:
            file = open(myfile,'rb') # open file , r => read , b => byte format
            response = file.read()
            file.close()
    
            header = 'HTTP/1.1 200 OK\n'
    
            if(myfile.endswith(".jpg")):
                mimetype = 'image/jpg'
            elif(myfile.endswith(".css")):
                mimetype = 'text/css'
            elif(myfile.endswith(".js")):
                mimetype = 'application/javascript'
            else:
                mimetype = 'text/html'
    
            header += 'Content-Type: '+str(mimetype)+'\n\n'
 
        except Exception as e:
            header = 'HTTP/1.1 404 Not Found\n\n'
            response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')
    
        final_response = header.encode('utf-8')
        final_response += response
        connection.send(final_response)
        connection.close()