# Yaks Assignment: YAK-3

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
curl -X GET http://127.0.0.1:5000/yak-shop/herd/T
```
or 

```
curl -X GET http://127.0.0.1:5000/yak-shop/herd/T
```
Output should be with status code 200 and a jsonified output is passed. 



This expects that 'load.xml' is a file in your current dir,
otherwise you should first load your herd and then make the GET request.

Like in a previous user story:
```
curl -X POST -d @herd.xml -H 'Content-Type: text/xml' http://localhost:5000/yak-shop/load
```


