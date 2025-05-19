from tkinter import *
from PIL import Image as PIL_Image
from PIL import ImageTk
import cv2

# Replace these with actual values
result_list = []  # Populate this with your actual results
path = "test.jpg"  # Path to your .jpg image file

def display_output():
    global path, result_list

    root = Tk()
    root.title("Fake Currency Detection System")

    window_width = 1100
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    root.resizable(False, False)

    main_frame = Frame(root, relief=GROOVE, bd=1)
    main_frame.place(x=10, y=10)

    canvas = Canvas(main_frame)
    master_frame = Frame(canvas)

    scrollbar = Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left")
    canvas.create_window((0, 0), window=master_frame, anchor='nw')

    def scrollbar_function(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=1050, height=550)

    master_frame.bind("<Configure>", scrollbar_function)

    # GUI frames
    sub_frame1 = Frame(master_frame, bg='black', pady=5)
    sub_frame2 = Frame(master_frame, bg='brown', pady=5, padx=5)
    sub_frame3 = Frame(master_frame, pady=5, padx=5)
    sub_frame4 = Frame(master_frame, pady=5, padx=5)

    sub_frame1.grid(row=1, column=1, padx=5, pady=5)
    sub_frame2.grid(row=2, column=1, padx=5, pady=5)
    sub_frame3.grid(row=3, column=1, padx=5, pady=5)
    sub_frame4.grid(row=4, column=1, padx=5, pady=5)

    title = Label(sub_frame1, text="FAKE CURRENCY DETECTION SYSTEM", fg='dark blue', font="Verdana 28 bold")
    title.pack()

    canvas_input = Canvas(sub_frame2, width=675, height=300)
    canvas_input.pack()

    if len(path) > 0 and path.lower().endswith('.jpg'):
        image = cv2.imread(path)
        if image is not None:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (675, 300))
            image = PIL_Image.fromarray(image)
            image = ImageTk.PhotoImage(image)

            canvas_input.image = image
            canvas_input.create_image(0, 0, anchor=NW, image=image)

    # Dummy feature display (you can update it based on your actual structure of result_list)
    pass_count = 0
    for i in range(10):
        frame = Frame(sub_frame4, bg='lightblue', padx=10, pady=10, relief=RIDGE, borderwidth=2)
        frame.grid(row=i // 3, column=i % 3, padx=10, pady=10)
        Label(frame, text=f"Feature {i+1}", font="Verdana 12 bold").pack()
        Label(frame, text=f"Status: {'PASS' if i % 2 == 0 else 'FAIL'}", fg='green' if i % 2 == 0 else 'red').pack()
        if i % 2 == 0:
            pass_count += 1

    result_label = Label(sub_frame3, text=f"RESULT: {pass_count} / 10 features PASSED!",
                         fg='green', font="Verdana 24 bold")
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    display_output()