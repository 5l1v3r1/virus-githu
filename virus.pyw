# imported the requests library
import requests
image_url = "https://the.earth.li/~sgtatham/putty/latest/w32/putty.exe"
 
# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object
 
# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("python_logo.exe",'wb') as f:

    # Saving received content as a png file in
    # binary format
 
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)
    self.root.withdraw()
