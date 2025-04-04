# **Decrypt Message from Space** 🚀

An encrypted message has been received from space! Your task is to decrypt it by following simple encoding rules. This Python program efficiently deciphers encrypted messages that follow a structured format.

## **Repository Information**
- **Main Repository:** [Programming Challenges](https://github.com/saleh-ato/programming-challenges)
- **Folder Path:** `1.decrypt-message-from-space/`
- **Author:** [Saleh Ato](https://github.com/saleh-ato)

---

## **Project Overview**
This repository provides a Python function, `spaceMessage()`, which decrypts encrypted space-transmitted messages that adhere to specific encoding rules:

- **Message Format:** Messages consist only of **capital letters, numbers, and square brackets (`[]`)**.
- **Repetition Rule:** Numbers before letters inside brackets indicate **repetition**:
  - Example: `"AB[3CD]"` → `"ABCDCDCD"` (repeats `"CD"` **3** times).
- **Nested Structure:** Messages can contain **multiple embedded brackets**.
- **Final Output:** Contains **only capital letters** after full decryption.

---

## **Example Usage**
### **Input/Output Examples**
```python
spaceMessage("ABCD")  
# Output: "ABCD"

spaceMessage("AB[3CD]")  
# Output: "ABCDCDCD"

spaceMessage("IF[2E]LG[5O]D")  
# Output: "IFEELGOOOOOD"

spaceMessage("[3BG]USBB[2DA]")  
# Output: "BGBGBGUSBBDADA"

spaceMessage("[3BG]USBB[2Da]")  
# Output: "Your message is not standard!"
```

---

## **Implementation Approach**
### **Key Features**
- **Validation:** Ensures messages contain only valid characters (`A-Z`, `0-9`, `[]`).
- **Regex-Powered Decryption:** Uses **regular expressions (`re` module)** for efficient pattern matching and expansion.
- **Iterative Replacement:** Processes **nested brackets** from inside out for correct message expansion.

### **Core Functions**
#### 1️⃣ `is_standard(message)`
- Ensures the message only contains **valid** characters.
- Returns `True` if valid, `False` otherwise.

#### 2️⃣ `spaceMessage(message)`
- **Validates** input using `is_standard()`.
- Extracts and **decodes** bracketed sequences iteratively.
- Uses **regex substitution (`re.sub`)** to expand encoded segments.
- Processes **nested** layers efficiently.

---

## **Setup and Installation**
### **Prerequisites**
Ensure you have **Python 3.x** installed.

### **Clone the Repository**
```sh
git clone https://github.com/saleh-ato/programming-challenges.git
cd programming-challenges/1.decrypt-message-from-space
```

### **Run the Script**
```sh
python app.py
```

---

## **How to Contribute**
We welcome contributions! Follow these steps:
1. **Fork** this repository.
2. **Create a new branch** (`git checkout -b feature-xyz`).
3. Implement your **feature or fix**.
4. **Commit** and **push** (`git push origin feature-xyz`).
5. Submit a **pull request**!

### **Possible Enhancements**
- Adding **support for deeper nested brackets**.
- Further optimizing **regex-based message expansion**.
- Creating a **GUI tool** for interactive decoding.

---

## **License**
This project is licensed under the **MIT License** – feel free to modify and expand!

---

## **Author**
Developed by [Saleh Ato](https://github.com/saleh-ato). Feel free to connect and contribute!
