import tkinter as tk
from GUI import OBSHitPointSyncForm
from functions import start_websocket

def main():
    root = tk.Tk()

    def on_submit(ws_url, sources, filter_name, character_id):
        start_websocket(ws_url, sources, filter_name, character_id)

    app = OBSHitPointSyncForm(root, on_submit)
    root.mainloop()

if __name__ == "__main__":
    main()