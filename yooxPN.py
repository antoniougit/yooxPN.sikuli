campaignName = input("Please enter campaign name:")
linkURL = input("Please enter deeplink URL:")
variantNum = int(input("Please enter number of variants:"))
variantContent = []
for i in range(variantNum):
    if i == 0:
        variantContent.append(input("Please enter content for Control:"))
    else:
        variantContent.append(input("Please enter content for Variant #"+str(i)+":"))
switchApp("Google Chrome")
click("1631282368774.png")
sleep(1)
for i in range(len(variantContent)):
    if i == 0:
        variantName = "ctrl"
        doubleClick("1631275177860.png")
    else: 
        variantName = "v" + str(i)
        if i == 1:
            doubleClick("1631275160823.png")
        elif i == 2:
            doubleClick("1631275693728.png")
        elif i == 3:
            doubleClick("1631275709369.png")
        elif i == 4:
            doubleClick("1631275723520.png")
        elif i == 5:
            doubleClick("1631275738175.png")
        elif i == 6:
            doubleClick("1631275746946.png")
        elif i == 7:
            type(Key.PAGE_DOWN)
            doubleClick("1631275761808.png")
        else:
            type(Key.PAGE_DOWN)
            doubleClick("1631275791572.png")
            break
    click("1631262246734.png")
    click("1631262265870.png")
    wait("1631262891654.png",10)
    click("1631262396549.png")
    type("a", KeyModifier.CTRL)
    type(Key.BACKSPACE)
    paste(variantName)
    click("1631263116877.png")
    wait(Pattern("1631277267272.png").similar(0.90).targetOffset(484,0),60)
    click(Pattern("1631277267272.png").similar(0.90).targetOffset(484,0))
    click("1631264418445.png")
    click(Pattern("1631264435642.png").similar(0.90))
    sleep(0.2)
    click(Pattern("1631277353712.png").similar(0.90).targetOffset(500,-1))
    type("f", KeyModifier.CTRL)
    type(Key.BACKSPACE)
    paste(campaignName + "_" + variantName)
    click(Pattern("1631265244840.png").targetOffset(0,2))
    sleep(0.2)
    click(Pattern("1631276451846.png").similar(0.90).targetOffset(483,-3))
    type("f", KeyModifier.CTRL)
    type(Key.BACKSPACE)
    paste("SWRVE_ID")
    click(Pattern("1631265244840.png").targetOffset(0,2))
    sleep(0.2)
    click(Pattern("1631265762597.png").similar(0.90).targetOffset(48,-1))
    paste(variantContent[i])
    type(Key.PAGE_DOWN)
    click(Pattern("1631266166509.png").similar(0.90).targetOffset(74,0))
    paste(linkURL)
    type(Key.PAGE_DOWN)
    click("1631266415356.png")
    wait(Pattern("1631266516087.png").similar(0.90))
    click(Pattern("1631266580615.png").similar(0.90).targetOffset(39,-35))
    sleep(0.2)
    click("1631262265870.png")