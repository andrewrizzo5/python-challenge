import pandas as pd

# File path to the election data
file_path = 'python-challenge/PyPoll/election_data.csv'

# Load the election data
election_data = pd.read_csv(file_path)

# Calculate the total number of votes cast
total_votes = election_data['Voter ID'].count()

# Get a complete list of candidates who received votes
candidates = election_data['Candidate'].unique()

# Initialize a dictionary to hold each candidate's vote count
candidate_votes = {candidate: 0 for candidate in candidates}

# Count the votes for each candidate
for candidate in election_data['Candidate']:
    candidate_votes[candidate] += 1

# Calculate the percentage of votes each candidate won and determine the winner
winner = None
max_votes = 0
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    if votes > max_votes:
        max_votes = votes
        winner = candidate
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")