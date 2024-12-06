import random

# List of participants
participants = [
    "Eliddinn", "Paul", "Astoriacanada", "Mog", "sarah",
    "Mincherz", "Byfield", "Anna", "TheCarrotBandit", 
    "JP", "Veeyno", "KrispyChew"
]

def secret_santa(participants):
    while True:
        # Create a copy of participants to manipulate
        receivers = participants.copy()
        random.shuffle(receivers)
        
        # Check unique conditions
        used_receivers = set()
        pairs = []
        valid_draw = True
        
        for giver in [p for p in participants if p != "Mog"]:
            for receiver in receivers:
                if giver != receiver and receiver not in used_receivers:
                    pairs.append((giver, receiver))
                    used_receivers.add(receiver)
                    receivers.remove(receiver)
                    break
            else:
                valid_draw = False
                break
        
        # Add Mog's receiver
        if valid_draw:
            mog_receiver = [r for r in participants if r != "Mog" and r not in used_receivers][0]
            pairs.append(("Mog", mog_receiver))
            return pairs

# Run the pairing and display the results
pairs = secret_santa(participants)
print("Secret Santa Pairs:")
for giver, receiver in pairs:
    print(f"{giver} → {receiver}")