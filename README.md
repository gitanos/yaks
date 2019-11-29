# Yaks Assignment: YAK-1

# Installation

Please run the following command within the context of an active virtual environment: 

```
pip3 install -r requirements.txt
```

# Execution

Make sure you have an .xml file to feed to the program or
 an XML formatted string to pass in the request. 

Start the program by running (in the project path)

```
python3 wsgi.py
```

This will instantiate a server running on localhost:5000.

You can now make an HTTP request to the server: 

```
curl -X POST -d @herd.xml -H 'Content-Type: text/xml' http://localhost:5000/yak-shop/load
```
(this supposes that 'herd.xml' is a file in your current dir)

Output should be with status code 205. 
HTTP Status Code 205 will overwrite the load.xml file in your repo. 

