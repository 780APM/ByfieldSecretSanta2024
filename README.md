# 🎄 Secret Santa Pairing Script  

This Python script generates randomized and fair Secret Santa pairings for a group of participants. It ensures that no one is matched with themselves and supports custom rules for specific participants.  

---

## 🛠 Features  

- **Randomized Matching**: Uses Python's `random.shuffle()` to randomize recipient assignments.  
- **Unique Pairing**: Ensures no participant is paired with themselves.  
- **Custom Rules**: Supports unique conditions (e.g., specific participants needing special handling).  
- **Validation**: Automatically retries until a valid draw is found.  

---

## 📜 Practices and Techniques  

- **Randomization**:  
  The script employs `random.shuffle()` to shuffle the recipient list, ensuring fair pairings.  

- **Error Handling**:  
  A `while True` loop allows the script to retry draws until a valid pairing is achieved, avoiding incomplete or invalid matches.  

- **Custom Logic**:  
  Implements flexible rules for participants requiring unique handling while maintaining fairness for the group.  

- **Data Structures**:  
  - `list`: For storing and manipulating participants and receivers.  
  - `set`: To efficiently track already assigned recipients.  

---

## 🔧 How to Use  

1. Clone or download this repository.  
2. Install Python 3.x if not already installed.  
3. Modify the `participants` list in the script to include your group members.  
4. Run the script:  
   ```bash
   python secret_santa.py

