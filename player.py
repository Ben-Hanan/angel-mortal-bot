from utils import getPlayers

class Player():
	def __init__(self):
		self.username = None
		self.angel = None
		self.mortal = None
		self.chat_id = None
		self.is_recipient_angel = None
	
def initialize_players(players_obj):
	all_players = getPlayers()

	for line in all_players:
		username = line["user"]
		angel = line["angel"]
		mortal = line["mortal"]
		chat_id = line["chat_id"]

		players_obj[username].username = username
		players_obj[username].angel = players_obj[angel]
		players_obj[username].mortal = players_obj[mortal]

		if chat_id:
			players_obj[username].chat_id = chat_id
		else:
			print(f'No chat ID found from for {username} from the Google Sheets')