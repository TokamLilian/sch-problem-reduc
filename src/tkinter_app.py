import tkinter as tk
from urllib import request
from tkinterweb import TkinterWeb

def open_tkinter_app():
    root = TkinterWeb()
    
    #root = tk.Tk()
    # Fetch HTML content from the Flask app
    # url = 'http://127.0.0.1:5001/'
    # response = request.urlopen(url)
    # html_content = response.read().decode('utf-8')
    
    # Display HTML content in a Tkinter label
    #label = tk.Label(root, text=html_content, justify=tk.LEFT)
    # label.pack()

    root.geometry("1000x800")

    # Load the Flask app URL
    root.load_url("http://127.0.0.1:5001/")
    root.mainloop()

if __name__ == "__main__":
    open_tkinter_app()