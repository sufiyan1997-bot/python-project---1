# Interactive Personal Data Collector

**Interactive Personal Data Collector** ek simple aur informative Python command-line application hai. Yeh script user se unka basic personal data (jaise naam, umar, height, aur favourite number) collect karti hai, use sahi data types me convert karti hai, aur un values ke saath-saath unke **Python Data Types** aur **Memory Addresses (`id()`)** ko screen par display karti hai.

## 🚀 Features

*   **Dynamic Data Input:** User se string, integer, aur float type ka data accept karta hai.
*   **Type & Memory Inspection:** Python ke built-in `type()` aur `id()` functions ka use karke variables ki internal details dikhata hai.
*   **Smart Calculation:** User ki current age ke basis par unka tentative **Birth Year** calculate karta hai.

---

## 🛠️ Requirements

*   **Python 3.x** aapke system par installed hona chahiye.

---

## 💻 How to Run the Script

Aap is script ko apne terminal ya command prompt ke zariye aasani se chala sakte hain:

1.  Sabse pehle, code ko ek file me save karein, jaise: `data_collector.py`
2.  Apna terminal open karein aur us directory (folder) me jayein jahan file saved hai.
3.  Neeche diye gaye command ko run karein:

```bash
python data_collector.py
```

---

## 📊 Sample Output Example

Jab aap script run karenge, toh console par output kuch is tarah dikhai dega:

```text
Welcome to the Interactive Personal Data Collector!

Please enter your name: Amit
Please enter your age: 25
Please enter your height in meters: 1.75
Please enter your favourite number: 7

Thank you! Here is the information we collected:

Name: Amit (Type: <class 'str'>, Memory Address: 140234567890)
Age: 25 (Type: <class 'int'>, Memory Address: 140234561234)
Height: 1.75 (Type: <class 'float'>, Memory Address: 140234565678)
Favourite Number: 7 (Type: <class 'int'>, Memory Address: 140234561111)

Your birth year is approximately: 2001 (based on your age of 25)

Thank you for using the Personal Data Collector. Goodbye!
```

---

## 📝 Code Overview

*   `input()`: User se data lene ke liye.
*   `int()` & `float()`: Input string ko numeric types me badalne ke liye.
*   `id()`: Python memory me object ka unique address check karne ke liye.
