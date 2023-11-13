import mss.tools
import time

time.sleep(10)

with mss.mss() as sct:
    monitor_info = sct.monitors[0]
    top_margin = monitor_info["height"] // 3
    monitor = {"top": monitor_info["top"] + top_margin, "left": monitor_info["left"], "width": monitor_info["width"], "height": (monitor_info["height"] * 2 // 3)-55}

    for i in range(1, 21):
        output = f"samples/{i}.png".format(**monitor)
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(f"Captured {output}")
        time.sleep(1)