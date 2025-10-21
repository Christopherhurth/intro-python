import csv


def read_csv(file_path):    
    """Reads a CSV file and returns its content as a list of dictionaries.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries representing the rows in the CSV file.
    """
    with open(file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        players = []
        for row in reader:
            players.append(row)
        return players

def write_csv(file_path, players, fieldnames):    
    """Writes a list of dictionaries to a CSV file.

    Args:
        file_path (str): The path to the CSV file.
        data (list): A list of dictionaries representing the rows to be written.

    """
    with open(file_path, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(players)

# Example usage, data will be a list of dictionaries:
file_path = 'players.csv'
players = read_csv(file_path)
for player in players:
    print(player) # each row is a dictionary
    
print(players[0]['name'])  # Example of accessing a specific field
players[0]['name'] = 'New Name'  # Example of modifying a specific field

# set the fieldnames for writing and send to write_csv
fieldnames = ['name', 'jersey', 'atbats', 'hits']
write_csv('players.csv', players, fieldnames)

# Display the updated data with numbers for each player
# if you use this line to show the player data, you will need to add the batting average (hits/atbats)
for number, player in enumerate(players, start=1):
    print(f"{number}: {player['name']}, Jersey: {player['jersey']}, At Bats: {player['atbats']}, Hits: {player['hits']}")
    


