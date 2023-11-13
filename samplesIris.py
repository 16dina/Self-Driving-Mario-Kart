import mss.tools
import time
import uuid
import keyboard
with mss.mss() as sct:
    # Get information of monitor 2
    monitor_number = 1
    monitor_info = sct.monitors[monitor_number]
    # The screen part to capture
    top_margin = monitor_info["height"] // 3                    

    monitor = {
        "top": monitor_info["top"] + top_margin,
        "left": monitor_info["left"]+55, 
        "width": monitor_info["width"]-120, 
        "height": monitor_info["height"] // 2,
        "mon": monitor_number,
    }
    while not keyboard.is_pressed('space'):
        output = f"ScreenIris/{str(uuid.uuid4())}.png".format(**monitor)
    # Grab the data
        sct_img = sct.grab(monitor) 

    # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)
        time.sleep(1)
    