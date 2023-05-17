import tkinter as tk
import joblib
import numpy as np
model = joblib.load('student_mark_predictor.pkl')
def submit():
    hoursinp = entry.get()
    hours = np.array([float(entry.get())]) 
    hours_2d = hours.reshape(-1, 1)  
    output = model.predict(hours_2d)[0].round(2)
    result_label.config(text="Bạn sẽ nhận được " +str(output)+" điểm khi bạn cố gắng học hành " + hoursinp + " tiếng đồng hồ")

root = tk.Tk()
root.geometry("500x200")  

label = tk.Label(root, text="Nhập thời gian bạn học:")
label.pack()

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Nhấn đi", command=submit)
submit_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()