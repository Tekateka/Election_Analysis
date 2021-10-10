# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes. 
candidate_options = []
candidate_votes = {}

# 1:County list and county votes dictionary.
county_list = []
county_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
Largest_county_turnout = ""
largest_county_vote = 0
winning_county_percentage = 0

# Read the csv and convert it into a list of dictionaries 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # For each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]

    # 3: Extract the county name from each row.
        county_name = row[1]
        
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:
        # 4b: Add the existing county to the list of counties..
            county_list.append(county_name)
         # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
    # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)


    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        county_vote = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        county_percentage = float(county_vote) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {county_percentage:.1f}% ({county_vote:,})\n")

        # # 6d: Print the county results to the terminal.
        print(county_results, end="")

        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
        
     # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_vote > largest_county_vote):
            Largest_county_turnout = county_name
            largest_county_vote = county_vote
            winning_county_percentage = county_percentage

    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {Largest_county_turnout}\n"
        f"Winning county Percentage: {winning_county_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)
    # Save the final candidates vote count to the rext filr 
    for candidate_name in candidate_votes:
    #  Retrieve vote count and percentage 
        candidate_vote = candidate_votes[candidate_name]
        vote_percentage = float(candidate_vote) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({candidate_vote:,})\n")
    # Print each candidate's voter count and percentage to the terminal 
        print(candidate_results)
    # Save the candidates results to the text fiel 
        txt_file.write(candidate_results)

    # Determine winning vote count, winning percentage, and winning candidate.
        if (candidate_vote > winning_count) and (vote_percentage > winning_percentage):
            winning_count = candidate_vote
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
    
    
