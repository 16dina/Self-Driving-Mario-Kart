import mss.tools

with mss.mss() as sct:
    monitor_info = sct.monitors[0]
    # The screen part to capture
    monitor = {"top": monitor_info["top"] + monitor_info["height"] // 2, "left": monitor_info["left"], "width": monitor_info["width"], "height": monitor_info["height"] // 2}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)
