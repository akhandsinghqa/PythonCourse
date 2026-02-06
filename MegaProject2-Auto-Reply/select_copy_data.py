import time

import pyautogui
import pyperclip

# Variables to store our coordinates
start_pos = (1004, 569)
end_pos = (1693, 770)
reply_pos = (1041, 920)


def copy_data():
    if start_pos and end_pos:
        time.sleep(0.5)

        pyautogui.moveTo(start_pos[0], start_pos[1])
        pyautogui.dragTo(end_pos[0], end_pos[1], duration=0.5, button='left')

        pyautogui.hotkey('ctrl', 'c')

        time.sleep(0.2)

        final_text = str(pyperclip.paste())
        # print("Copied text : \n",final_text)
        return final_text


def paste_data(reply: str):
    pyautogui.moveTo(reply_pos[0], reply_pos[1])
    pyautogui.click(reply_pos[0], reply_pos[1])

    pyautogui.write(reply)

    time.sleep(5)

    pyautogui.press('enter')
