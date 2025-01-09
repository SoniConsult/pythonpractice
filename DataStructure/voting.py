def voting_system():
    voters = set()
    votes = {} 

    print("Welcome to the Voting System!")
    print("Enter 'stop' to end the voting process.")
    
    while True:
        voter_id = input("Enter your voter ID: ")
        if voter_id.lower() == 'stop':
            break
        if voter_id in voters:
            print("You have already voted! Voting not allowed twice.")
            continue
        candidate = input("Enter the candidate's name you want to vote for: ")
        
        voters.add(voter_id)
        
        if candidate in votes:
            votes[candidate] += 1
        else:
            votes[candidate] = 1

        print(f"Vote registered for {candidate}.")

    print("\nVoting process ended.")
    print("Results:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")

voting_system()
