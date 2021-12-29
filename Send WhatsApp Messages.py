import pywhatkit as kit

Number = "+551199999999"
Message = "Testing"
Timehrs = 23
TimeMinutes = 59

# kit.sendwhatmsg(Number, Message, Timehrs, TimeMinutes)
kit.sendwhatmsg_instantly(Number, Message)
