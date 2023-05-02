import pywhatkit as kit

# To what number the message will be send
Number = "++5511992937099"

# What will be the message
Message = "Testing"

# Assign the time for when the message will be sent
Timehrs = 23
TimeMinutes = 59

# Send the message at the specified time
# kit.sendwhatmsg(Number, Message, Timehrs, TimeMinutes)

# Send the message instantly
kit.sendwhatmsg_instantly(Number, Message)
