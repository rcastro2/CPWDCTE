import os
open("images.js", 'w').write("var thumbs = [" + ',\n'.join(["'images/events/thumbs/%s'"%file for file in os.listdir(os.getcwd()) if file.lower().endswith(".jpg") ]) + "]")
    
