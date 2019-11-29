# Yaks Assignment: YAK-4

# Installation

Please run the following command within the context of an active virtual environment: 

```
pip3 install -r requirements.txt
```

# Execution

Start the program by running (in the project path)

```
python3 wsgi.py
```

This will instantiate a server running on localhost:5000.

You can now make an HTTP request to the server: 

```
curl -X POST -H "Content-Type: application/json" -d <your-json-here> http://127.0.0.1:5000/yak-shop/order/T```

```

This expects that 'load.xml' is a file in your current dir,
otherwise you should first load your herd and then make the GET request.

Like in a previous user story:
```
curl -X POST -d @herd.xml -H 'Content-Type: text/xml' http://localhost:5000/yak-shop/load
```


