import json

enc='utf-8'
file  =  open('eventsData.html', 'r', encoding=enc).read()
#print(file)
events = []
pos = 0
for e in range(51):
    #Find Title
    sp = file.index("<span >",pos) + len("<span >")
    ep = file.index("</span >",sp)
    title = file[sp:ep]
    print(title)

    #Find Date
    sp = file.index("<date>",ep) + len("<date>")
    ep = file.index("</date>",sp)
    date = file[sp:ep]
    #print(date)

    #Find Mainpic
    sp = file.index("src=\"",ep) + len("src=\"")
    ep = file.index("\"",sp)
    mainpic = file[sp:ep]
    #print(mainpic)

    #Find description
    sp = file.index("<description>",ep) + len("<description>")
    ep = file.index("<link>",sp)
    description = file[sp:ep].replace("\n","").replace("\t","")
    #print(description)
    
    #Find Gallery
    isp = file.index("<gallery>",ep) + len("<gallery>")
    ep = file.index("</gallery>",isp)
    iep = isp
    gallery=[]
    while isp < ep:
        #Find Image
        isp = file.index("src=\"",iep) + len("src=\"")
        iep = file.index("\"",isp)
        img = None
        if isp < ep:
            img = file[isp:iep]
        if img != None: gallery.append({"thumbnail":img})
    pos = ep
    #print(pos)

    events.append({"title":title,"date":date,"image":mainpic,"description":description,"gallery":gallery})

with open("events.js","w") as fp:
    json.dump(events, fp)

