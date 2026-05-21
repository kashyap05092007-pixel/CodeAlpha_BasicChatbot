# CodeAlpha_BasicChatbot



---

# 1️⃣ Import Datetime Module

```python id="j1e4tx"
import datetime
```

## ✅ Explanation

`datetime` module is used to get:

* Current Time
* Current Date

Example:

```txt id="grjmbn"
10:30:15
21-05-2026
```

---

# 2️⃣ Create Chatbot Function

```python id="jlwmn7"
def chatbot_response(user_input):
```

## ✅ Explanation

A **function** is used to organize chatbot replies.

* Function Name:

```txt id="jlwmnc"
chatbot_response
```

* It takes user message as input.

---

# 3️⃣ Convert Input to Lowercase

```python id="jlwmne"
user_input = user_input.lower()
```

## ✅ Explanation

Converts all text into lowercase.

Example:

```txt id="jlwmng"
HELLO → hello
Hi → hi
```

This helps chatbot understand input easily.

---

# 4️⃣ Create Greeting List

```python id="jlwmni"
greetings = ["hello", "hi", "hey"]
```

## ✅ Explanation

A list stores greeting words.

Example:

```txt id="jlwmnk"
hello
hi
hey
```

---

# 5️⃣ Greeting Condition

```python id="jlwmnm"
if user_input in greetings:
```

## ✅ Explanation

Checks whether user typed:

* hello
* hi
* hey

If true:

```python id="jlwmno"
return "Hello! 👋 Nice to meet you."
```

---

# 6️⃣ How Are You Condition

```python id="jlwmnq"
elif "how are you" in user_input:
```

## ✅ Explanation

Checks whether sentence contains:

```txt id="jlwmns"
how are you
```

Bot Reply:

```txt id="jlwmnu"
I'm fine and ready to help you!
```

---

# 7️⃣ Name Condition

```python id="jlwmnw"
elif "your name" in user_input:
```

## ✅ Explanation

Checks if user asks chatbot name.

Example:

```txt id="jlwmny"
what is your name
```

---

# 8️⃣ Time Feature

```python id="jlwmo0"
elif "time" in user_input:
```

## ✅ Explanation

Checks if user asks current time.

---

## Get Current Time

```python id="jlwmo2"
current_time = datetime.datetime.now().strftime("%H:%M:%S")
```

## ✅ Explanation

### `datetime.now()`

Gets current system time.

### `strftime()`

Formats time.

Format:

```txt id="jlwmo4"
Hour : Minute : Second
```

Example:

```txt id="jlwmo6"
10:45:30
```

---

# 9️⃣ Date Feature

```python id="jlwmo8"
elif "date" in user_input:
```

## ✅ Explanation

Checks if user asks current date.

---

## Get Current Date

```python id="jlwmoa"
current_date = datetime.datetime.now().strftime("%d-%m-%Y")
```

## ✅ Explanation

Format:

```txt id="jlwmoc"
Day-Month-Year
```

Example:

```txt id="jlwmoe"
21-05-2026
```

---

# 🔟 Help Command

```python id="jlwmog"
elif "help" in user_input:
```

## ✅ Explanation

Displays available chatbot commands.

Output:

```txt id="jlwmoi"
hello
time
date
bye
```

---

# 1️⃣1️⃣ Bye Condition

```python id="jlwmok"
elif user_input == "bye":
```

## ✅ Explanation

Checks if user wants to exit chatbot.

Bot Reply:

```txt id="jlwmom"
Goodbye!
```

---

# 1️⃣2️⃣ Unknown Input

```python id="jlwmoo"
else:
```

## ✅ Explanation

Runs when chatbot doesn't understand message.

Example:

```txt id="jlwmoq"
asdjkl
weather today
```

Bot Reply:

```txt id="jlwmos"
Sorry, I don't understand that.
```

---

# 1️⃣3️⃣ Print Title

```python id="jlwmou"
print("ADVANCED CHATBOT")
```

## ✅ Explanation

Displays chatbot heading.

Output:

```txt id="jlwmow"
🤖 ADVANCED CHATBOT
```

---

# 1️⃣4️⃣ Chat Loop

```python id="jlwmoy"
while True:
```

## ✅ Explanation

Infinite loop keeps chatbot running continuously.

---

# 1️⃣5️⃣ User Input

```python id="jlwmp0"
user_message = input("\nYou: ")
```

## ✅ Explanation

Takes message from user.

Example:

```txt id="jlwmp2"
hello
```

---

# 1️⃣6️⃣ Empty Input Check

```python id="jlwmp4"
if user_message.strip() == "":
```

## ✅ Explanation

### `strip()`

Removes spaces.

Checks if user entered nothing.

Wrong:

```txt id="jlwmp6"

(space only)
```

---

# 1️⃣7️⃣ Get Bot Response

```python id="jlwmp8"
response = chatbot_response(user_message)
```

## ✅ Explanation

Calls chatbot function and gets reply.

Example:

```txt id="jlwmpa"
hello → Hi!
```

---

# 1️⃣8️⃣ Print Bot Reply

```python id="jlwmpc"
print("Bot:", response)
```

## ✅ Explanation

Displays chatbot answer.

Output:

```txt id="jlwmpe"
Bot: Hello!
```

---

# 1️⃣9️⃣ Exit Loop

```python id="jlwmpg"
if user_message.lower() == "bye":
    break
```

## ✅ Explanation

Stops chatbot when user types:

```txt id="jlwmpi"
bye
```

---

# 2️⃣0️⃣ Ending Message

```python id="jlwmpk"
print("Chatbot Program Ended")
```

## ✅ Explanation

Displays final program ending message.

---

# 📚 Concepts Used

| Concept        | Purpose                |
| -------------- | ---------------------- |
| Function       | Organize chatbot logic |
| if-elif        | Conditions             |
| while loop     | Continuous chatting    |
| List           | Store greetings        |
| datetime       | Current time/date      |
| string methods | Text handling          |
| input/output   | User interaction       |

---

# 💻 Example Output

```txt id="jlwmpm"
🤖 ADVANCED CHATBOT

You: hello
Bot: Hello! 👋 Nice to meet you.

You: time
Bot: ⏰ Current Time is: 10:45:30

You: date
Bot: 📅 Today's Date is: 21-05-2026

You: bye
Bot: Goodbye! 👋
```
