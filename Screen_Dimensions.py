import tkinter as tk

# إنشاء نافذة Tkinter
root = tk.Tk()

# الحصول على عرض وارتفاع الشاشة
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# طباعة الأبعاد
print(f"Screen Width: {screen_width}")
print(f"Screen Height: {screen_height}")

# إغلاق النافذة بعد الطباعة
root.quit()
