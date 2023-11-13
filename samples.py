import mss.tools
import time
import uuid

time.sleep(10)

with mss.mss() as sct:
    monitor_info = sct.monitors[0]
    top_margin = monitor_info["height"] // 3
    monitor = {"top": monitor_info["top"] + top_margin, "left": monitor_info["left"] + 55, "width": monitor_info["width"] - 120, "height": (monitor_info["height"] * 2 // 3)-55}

    for i in range(1, 21):
        output = f"dataset/{str(uuid.uuid4())}.png".format(**monitor)
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(f"Captured {output}")
        time.sleep(1)