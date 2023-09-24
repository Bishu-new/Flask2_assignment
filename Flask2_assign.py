#!/usr/bin/env python
# coding: utf-8

# Ans 1: The **GET** and **POST** methods are two different types of HTTP requests.
# 
# **GET Method**:
# - The GET method is used to request data from a specified resource.
# - It is mainly used at the client (Browser) side to send a request to a specified server to get certain data or resources.
# - Using this method, the server should only let us receive the data and not change its state.
# - The request parameter of the GET method is appended to the URL.
# - GET requests can be cached, remain in the browser history, and can be bookmarked.
# - GET requests should never be used when dealing with sensitive data.
# - GET requests have length restrictions.
# - GET requests are only used to request data (not modify).
# 
# **POST Method**:
# - The POST method is used to send data to a server to create/update a resource.
# - It is mainly used at the client (Browser) side to send data to a specified server in order to create or rewrite a particular resource/data.
# - This data sent to the server is stored in the request body of the HTTP request.
# - POST requests are never cached, do not remain in the browser history, and cannot be bookmarked.
# - POST requests have no restrictions on data length.
# - POST is a little safer than GET because the parameters are not stored in browser history or in web server logs.
# 

# Ans 2 : Why is request used in Flask?
# 
# The request object in Flask is used to access all the data sent from the client to the server12. This data can be recovered using the GET/POST methods. The request object holds all incoming data from the request, which includes the mimetype, referrer, IP address, raw data, HTTP method, and headers, among other things2. It’s a way for your Flask application to interact with incoming client requests and extract necessary information from them.

# Ans 3 : Why is redirect() used in Flask?
# 
# The redirect() function in Flask is used to send the user to a particular URL with a specific status code34. It’s a way of telling your app to take a different route5. For example, after a user logs in, you might want to redirect them to their dashboard. Or if they hit a route they’re not authorized to access, you might want to redirect them to an error page or back to the home page.

# Ans 4: What are templates in Flask? Why is the render_template() function used?
# 
# Templates in Flask are files that contain static data as well as placeholders for dynamic data6. They promote code organization, maintainability, and reusability by separating the presentation logic from the business logic. A template can be rendered with specific data to produce a final document.
# 
# The render_template() function in Flask is used to render these templates8910. Instead of rendering raw string or inline HTML code from the backend code to the browser, we can have a separate HTML file passed to the client. This function takes the name of a template file as its first argument and any number of keyword arguments representing values you want to insert into the template.

# Ans 5 : Create a simple API. Use Postman to test it. Attach the screenshot of the output in the Jupyter Notebook.

# In[ ]:


from flask import Flask , request , jsonify
app = Flask(__name__)

@app.route('/postman_data' , methods = ['GET'] )
def home():
    if(request.method == 'GET'):
        
         return "Hello, World!"

if __name__ == '__main__':
    app.run(host = "0.0.0.0")


# ![image.png](attachment:image.png)

# In[ ]:




