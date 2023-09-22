import pyautogui
import opencv

buttons = ['Player.png','Vote.png','Submit.png','Again.png','Counter.png']

#def networkError(): Refresh page to clear error

#def screenShot(): Take screenshots of buttons for user

def selectPlayer(player):
    buttons[0] = player + '.png' #this doesn't account for other image formats
    
def locateOnScreen():
    i = 0
    while i < len(buttons): 
        if pyautogui.locateCenterOnScreen(buttons[i], confidence = .95) is not None:
            x,y = pyautogui.locateCenterOnScreen(buttons[i], confidence = .95)
            pyautogui.click(x,y)
            i += 1

votes = 0
print('please enter player\'s last name to vote for.')
player = input()
selectPlayer(player)
while(True):
    locateOnScreen()
    votes +=1
    print('votes =',votes)
    
