import tkinter as tk  # For UI development
import requests  # For sending HTTP requests
import json  # For handling JSON data (optional)

window = tk.Tk()
window.title("HTTP Client")

url_label = tk.Label(window, text="Enter URL:")
url_label.pack()

url_entry = tk.Entry(window, width=50)
url_entry.pack()

method_label = tk.Label(window, text="Choose Method:")
method_label.pack()

method_var = tk.StringVar()
method_dropdown = tk.OptionMenu(window, method_var, "GET", "POST", "PUT", "DELETE")
method_dropdown.pack()

headers_label = tk.Label(window, text="Custom Headers (optional):")
headers_label.pack()

headers_entry = tk.Entry(window, width=50)
headers_entry.pack()

data_label = tk.Label(window, text="Request Data (optional):")
data_label.pack()

data_entry = tk.Text(window, width=50, height=5)
data_entry.pack()

def send_request():
    url = url_entry.get()
    method = method_var.get()
    headers_text = headers_entry.get()
    data = data_entry.get("1.0", tk.END).strip()

    headers = {}
    if headers_text:
        for header_pair in headers_text.splitlines():
            key, value = header_pair.split(":", 1)
            headers[key.strip()] = value.strip()

    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, data=data)
        elif method == "PUT":
            response = requests.put(url, headers=headers, data=data)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)

        response_text = response.text

        if response.headers['Content-Type'] == 'application/json':
            response_data = json.loads(response_text)
            response_text = json.dumps(response_data, indent=4)

        result_label.config(text=f"Response:\n{response_text}")

    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error: {e}")

send_button = tk.Button(window, text="Send Request", command=send_request)
send_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
