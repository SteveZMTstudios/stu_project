# modules
import os
from win10toast_click import ToastNotifier 

# function 
page_url = 'http://example.com/'

def open_url():
    try: 
        os.system('explorer F:\\')
        print('Opening URL...')  
    except: 
        print('Failed to open URL. Unsupported variable type.')

# initialize 
toaster = ToastNotifier()

# showcase
toaster.show_toast(
    "发现新硬件", # title
    "轻点此处 来打开u盘 >>", # message 
    icon_path=None, # 'icon_path' 
    duration=20, # for how many seconds toast should be visible; None = leave notification in Notification Center
    threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
    callback_on_click=open_url # click notification to run function 
    )
