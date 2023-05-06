import pywhatkit as kit


def sendWhatsAppMessage(Message, Number):
    # Send the message instantly
    kit.sendwhatmsg_instantly(Number, Message)


def sendWhatsAppMessageInTime(Message, Number, TimeHrs=23, TimeMinutes=59):
    # Send the message at the specified time
    kit.sendwhatmsg(Number, Message, TimeHrs, TimeMinutes)


sendWhatsAppMessage("Testing", "++5511992937099")
