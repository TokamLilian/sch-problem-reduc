import tkinter as tk
from tkhtmlview import HTMLLabel

class FlaskAppViewer(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Scheduling Reduction")
        self.geometry("1000x800")

        # Create an HTMLLabel to display the Flask app
        html_label = HTMLLabel(self)
        html_label.pack(fill=tk.BOTH, expand=True)

        # Load the Flask app content
        html_label.set_html('<iframe src="http://127.0.0.1:5001/" width="100%" height="100%"></iframe>')

if __name__ == "__main__":
    app_viewer = FlaskAppViewer()
    app_viewer.mainloop()