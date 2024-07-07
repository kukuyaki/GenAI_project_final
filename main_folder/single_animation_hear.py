import random
import tkinter as tk

# 初始变量
x = 1100
cycle = 0
check = 0  # 初始状态设置为idle
event_number = random.randint(1, 3)
impath = 'C:\\Users\\hiton\\OneDrive\\文件\\GenAI_final_product\\picture\\'
# 创建窗口
window = tk.Tk()
window.wm_attributes('-topmost', True)
window.geometry('128x128+' + str(x) + '+500')
label = tk.Label(window, bd=0, bg='black')
label.pack()

# 窗口配置
window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor', 'black')
# 定义动作
idle_gif = [tk.PhotoImage(file=impath + 'hear10c.gif', format='gif -index %i' % (i)) for i in range(10)]

# 确定事件
def event(cycle,  x):
    # print('idle')
    window.after(100, update, cycle,   x)  # idle
# 更新动画
def update(cycle,   x):
    frame = idle_gif[cycle]
    if cycle < len(idle_gif) - 1:
        cycle += 1
    else:
        cycle = 0
    label.configure(image=frame)
    window.after(1, event, cycle,  x)
    


# 启动动画

print('idle')
window.after(1, update, cycle, 1000)
window.mainloop()
