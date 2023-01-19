import webbrowser as wb

def webauto():
     chrome_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'# ADD THE BROWSER INSTALL ADDRESS
     URLS = {
            "youtube.com",
            "google.com",
            "stackoverflow.com"
     }
     for url in URLS:
         print("opening multiple taps:"+url)
         wb.get(chrome_path).open(url)
webauto()