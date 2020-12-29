import random

#--------------------------------------------------------------------------------------------------
# Globals
#--------------------------------------------------------------------------------------------------
sims = 100000

cash = 0
bet_size = 5

#--------------------------------------------------------------------------------------------------
# Odds / Payouts
#--------------------------------------------------------------------------------------------------
class RangeDict(dict): # Creates a dictionary that can hold a range of keys for a given value
    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)

fruitOdds = {
        range(0,5) : "🍒",
        range(5,30) : "🍇",
        range(30,52) : "🍓",
        range(52,67) : "🍋",
        range(67,79) : "🍉",
        range(79,89) : "🍑",
        range(89,97) : "🥑",
        range(97,101): "💎"
        }

fruits = RangeDict(fruitOdds)

payouts = {
	"🍒🍒🍒" : 10,
	"🍇🍇🍇" : 5,
	"🍓🍓🍓" : 10,
	"🍋🍋🍋" : 20,
	"🍉🍉🍉" : 30,
	"🍑🍑🍑" : 75,
	"🥑🥑🥑" : 100,
	"💎💎💎" : 150,
 	}

#--------------------------------------------------------------------------------------------------
# Slot Machine
#--------------------------------------------------------------------------------------------------
wins = []

for i in range(sims):
    reel = []

    cash -= bet_size

    # Pick 3 fruits
    for i in range(3):
        fruit = random.randint(0,100)
        slot = fruits[fruit]
        reel.append(slot)

    # Compares the reel to the preset payouts
    try:
    	payout = bet_size * payouts[''.join(reel)]
    	wins.append(''.join(reel))
    except KeyError:
    	payout = 0

    # Single / Double wins
    if reel.count("🍒") == 1:
        payout += bet_size * 2
        wins.append("🍒")

    if reel.count("🍒") == 2:
        payout += bet_size * 5
        wins.append("🍒🍒")

    if reel.count("💎") == 2:
        payout += bet_size * 50
        wins.append("💎💎")

    cash += payout

print(
                "\n💎💎💎| {}, {:0.3f}%".format(wins.count("💎💎💎"), wins.count("💎💎💎")/sims*100) +  
                "\n💎💎  | {}, {:0.3f}%".format(wins.count("💎💎"), wins.count("💎💎")/sims*100) + 
                "\n🥑🥑🥑| {}, {:0.3f}%".format(wins.count("🥑🥑🥑"), wins.count("🥑🥑🥑")/sims*100) + 
                "\n🍑🍑🍑| {}, {:0.3f}%".format(wins.count("🍑🍑🍑"), wins.count("🍑🍑🍑")/sims*100) + 
                "\n🍉🍉🍉| {}, {:0.3f}%".format(wins.count("🍉🍉🍉"), wins.count("🍉🍉🍉")/sims*100) + 
                "\n🍋🍋🍋| {}, {:0.3f}%".format(wins.count("🍋🍋🍋"), wins.count("🍋🍋🍋")/sims*100) + 
                "\n🍓🍓🍓| {}, {:0.3f}%".format(wins.count("🍓🍓🍓"), wins.count("🍓🍓🍓")/sims*100) + 
                "\n🍇🍇🍇| {}, {:0.3f}%".format(wins.count("🍇🍇🍇"), wins.count("🍇🍇🍇")/sims*100) + 
                "\n🍒🍒🍒| {}, {:0.3f}%".format(wins.count("🍒🍒🍒"), wins.count("🍒🍒🍒")/sims*100) + 
                "\n🍒🍒  | {}, {:0.3f}%".format(wins.count("🍒🍒"), wins.count("🍒🍒")/sims*100) + 
                "\n🍒    | {}, {:0.3f}%".format(wins.count("🍒"), wins.count("🍒")/sims*100))

print(cash)
