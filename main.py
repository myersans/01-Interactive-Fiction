import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
	"uuid": "9F526749-9497-40E5-9892-D6C310109EB9",
  "name": "Mummy Madness",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631056384358,
  "passages": [
    {
      "name": "The Trident Paths",
      "tags": "",
      "id": "1",
			"score":0,
      "text": "You awaken. Looking around your vision is very fuzzy and your entire being feels dry. Sand shifts beneath the weight of your body and blows softly in the wind. As your vision clears, the vast expanse of dunes comes into focus. Three faint pathes diverge ahead of you like a trident. One to the LEFT, RIGHT, and FORWARD.\n\n[[LEFT->Oasis]]\n[[FORWARD->Ancient Ruins]]\n[[RIGHT->Sphinx]]",
      "links": [
        {
          "linkText": "LEFT",
          "passageName": "Oasis",
          "original": "[[LEFT->Oasis]]"
        },
        {
          "linkText": "FORWARD",
          "passageName": "Ancient Ruins",
          "original": "[[FORWARD->Ancient Ruins]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "Sphinx",
          "original": "[[RIGHT->Sphinx]]"
        }
      ],
      "hooks": [],
      "cleanText": "You awaken. Looking around your vision is very fuzzy and your entire being feels dry. Sand shifts beneath the weight of your body and blows softly in the wind. As your vision clears, the vast expanse of dunes comes into focus. Three faint pathes diverge ahead of you like a trident. One to the LEFT, RIGHT, and FORWARD."
    },
    {
      "name": "Oasis",
      "tags": "",
      "id": "2",
			"score":10,
	    "text": "You come upon a peaceful oasis. It's waters sweet and the air is fresh. Another path leads to the RIGHT, while the one you are on leads FORWARD into the waters. You look behind yourself to see that you can RETURN to the trident paths as well.\n\n[[FORWARD->Underworld]]\n[[RIGHT->Ancient Ruins]]\n[[RETURN->The Trident Paths]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Underworld",
          "original": "[[FORWARD->Underworld]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "Ancient Ruins",
          "original": "[[RIGHT->Ancient Ruins]]"
        },
        {
          "linkText": "RETURN",
          "passageName": "The Trident Paths",
          "original": "[[RETURN->The Trident Paths]]"
        }
      ],
      "hooks": [],
      "cleanText": "You come upon a peaceful oasis. It's waters sweet and the air is fresh. Another path leads to the RIGHT, while the one you are on leads FORWARD into the waters. You look behind yourself to see that you can RETURN to the trident paths as well."
    },
    {
      "name": "Ancient Ruins",
      "tags": "",
      "id": "3",
			"score":10,
      "text": "Large pillars made of sturdy sandstone stand tall before you. This must have been a great temple. It appears to be uninhabited aside from a broken CART covered by a tarp. Perhaps a look INSIDE will reveal it's mysteries. Too much for you? No worries feel free to RETURN to the paths or the OASIS.\n\n[[RETURN->The Trident Paths]] \n[[CART->Cart]]\n[[INSIDE->The Temple Courtyard]]\n[[Oasis->Oasis]]",
      "links": [
        {
          "linkText": "RETURN",
          "passageName": "The Trident Paths",
          "original": "[[RETURN->The Trident Paths]]"
        },
        {
          "linkText": "CART",
          "passageName": "Cart",
          "original": "[[CART->Cart]]"
        },
        {
          "linkText": "INSIDE",
          "passageName": "The Temple Courtyard",
          "original": "[[INSIDE->The Temple Courtyard]]"
        },
        {
          "linkText": "Oasis",
          "passageName": "Oasis",
          "original": "[[Oasis->Oasis]]"
        }
      ],
      "hooks": [],
      "cleanText": "Large pillars made of sturdy sandstone stand tall before you. This must have been a great temple. It appears to be uninhabited aside from a broken CART covered by a tarp. Perhaps a look INSIDE will reveal it's mysteries. Too much for you? No worries feel free to RETURN to the paths or the OASIS."
    },
    {
      "name": "Sphinx",
      "tags": "",
      "id": "4",
			"score":10,
      "text": "Seemingly the only living creature in this wasteland, you come upon a sphinx. They are resting peacfully, or at least they were until you arrived to disturb them. They jump up with a jold and approach you. \"Mere mortal, why do you ditsturb my peace? No matter, this indescretion must be atoned for. Answer my riddle and I'll let you go.\" Will you ANSWER?\n\n[[ANSWER->Riddle]]\n[[RETURN->The Trident Paths]]",
      "links": [
        {
          "linkText": "ANSWER",
          "passageName": "Riddle",
          "original": "[[ANSWER->Riddle]]"
        },
        {
          "linkText": "RETURN",
          "passageName": "The Trident Paths",
          "original": "[[RETURN->The Trident Paths]]"
        }
      ],
      "hooks": [],
      "cleanText": "Seemingly the only living creature in this wasteland, you come upon a sphinx. They are resting peacfully, or at least they were until you arrived to disturb them. They jump up with a jold and approach you. \"Mere mortal, why do you ditsturb my peace? No matter, this indescretion must be atoned for. Answer my riddle and I'll let you go.\" Will you ANSWER?"
    },
    {
      "name": "Underworld",
      "tags": "",
      "id": "5",
			"score":10,
      "text": "However you got here, you know there is no way back. Anubis stands before you, he archs back and lets out a laugh from his snout. \"Hello mortal, we were destined to meet at some point. It's time we weighed your heart, FOLLOW me.\"\n\n[[FOLLOW->The Scales of Fate]]",
      "links": [
        {
          "linkText": "FOLLOW",
          "passageName": "The Scales of Fate",
          "original": "[[FOLLOW->The Scales of Fate]]"
        }
      ],
      "hooks": [],
      "cleanText": "However you got here, you know there is no way back. Anubis stands before you, he archs back and lets out a laugh from his snout. \"Hello mortal, we were destined to meet at some point. It's time we weighed your heart, FOLLOW me.\""
    },
    {
      "name": "Cart",
      "tags": "",
      "id": "6",
			"score":10,
      "text": "The broken cart appears just that, broken. What could be under that tarp if you LIFT it?\n\n[[RETURN->The Trident Paths]] \n[[LIFT->Mummy Attack]]",
      "links": [
        {
          "linkText": "RETURN",
          "passageName": "The Trident Paths",
          "original": "[[RETURN->The Trident Paths]]"
        },
        {
          "linkText": "LIFT",
          "passageName": "Mummy Attack",
          "original": "[[LIFT->Mummy Attack]]"
        }
      ],
      "hooks": [],
      "cleanText": "The broken cart appears just that, broken. What could be under that tarp if you LIFT it?"
    },
    {
      "name": "The Temple Courtyard",
      "tags": "",
      "id": "7",
			"score":10,
      "text": "The remains of what was once an ornate courtyard. The STATUE of a large jackal man takes centerpiece amongst the decay. Beyond him lies a STAIRCASE suprisinlgy lit by fresh torches. This is a tad creepy and you may want to consider RETURN if you feel the need.\n\n[[STATUE->Statue of Anubis]]\n[[STAIRCASE->Portal to the Underworld]]\n[[RETURN->Ancient Ruins]]",
      "links": [
        {
          "linkText": "STATUE",
          "passageName": "Statue of Anubis",
          "original": "[[STATUE->Statue of Anubis]]"
        },
        {
          "linkText": "STAIRCASE",
          "passageName": "Portal to the Underworld",
          "original": "[[STAIRCASE->Portal to the Underworld]]"
        },
        {
          "linkText": "RETURN",
          "passageName": "Ancient Ruins",
          "original": "[[RETURN->Ancient Ruins]]"
        }
      ],
      "hooks": [],
      "cleanText": "The remains of what was once an ornate courtyard. The STATUE of a large jackal man takes centerpiece amongst the decay. Beyond him lies a STAIRCASE suprisinlgy lit by fresh torches. This is a tad creepy and you may want to consider RETURN if you feel the need."
    },
    {
      "name": "Mummy Attack",
      "tags": "",
      "id": "8",
			"score":10,
      "text": "An unholy wrapped figure snarls at you from inside that cart and makes a grab for your hand. You should probably RUN.\n\n[[Run->Ancient Ruins]]",
      "links": [
        {
          "linkText": "RUN",
          "passageName": "Ancient Ruins",
          "original": "[[Run->Ancient Ruins]]"
        }
      ],
      "hooks": [],
      "cleanText": "An unholy wrapped figure snarls at you from inside that cart and makes a grab for your hand. You should probably RUN."
    },
    {
      "name": "Statue of Anubis",
      "tags": "",
      "id": "9",
			"score":10,
      "text": "The statue of Anubis holds out his hand. He seems welcoming in an off-putting way. Do you TAKE his hand?\n\n[[TAKE->Underworld]] \n[[RETURN->The Temple Courtyard]]",
      "links": [
        {
          "linkText": "TAKE",
          "passageName": "Underworld",
          "original": "[[TAKE->Underworld]]"
        },
        {
          "linkText": "RETURN",
          "passageName": "The Temple Courtyard",
          "original": "[[RETURN->The Temple Courtyard]]"
        }
      ],
      "hooks": [],
      "cleanText": "The statue of Anubis holds out his hand. He seems welcoming in an off-putting way. Do you TAKE his hand?"
    },
    {
      "name": "Portal to the Underworld",
      "tags": "",
      "id": "10",
			"score":10,
      "text": "These stairs no longer feel like stairs. As you descned deeper and deeper into the earth, you realize there is no choice but to press FORWARD.\n\n[[FORWARD->Underworld]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Underworld",
          "original": "[[FORWARD->Underworld]]"
        }
      ],
      "hooks": [],
      "cleanText": "These stairs no longer feel like stairs. As you descned deeper and deeper into the earth, you realize there is no choice but to press FORWARD."
    },
    {
      "name": "Riddle",
      "tags": "",
      "id": "11",
			"score":10,
      "text": "The sphinx peers deep into your eyes as if to study your very soul. \"What is heavy, but not backwards?\" You ponder your choices, what could it be? Perhaps its TON, LIGHT, or HEAVY. \"Choose wisely mortal, or you may find yourself in a realm most unpleasent.\n\n[[LIGHT->Underworld]] \n[[HEAVY->Underworld]] \n[[TON->Sandstorm]]",
      "links": [
        {
          "linkText": "LIGHT",
          "passageName": "Underworld",
          "original": "[[LIGHT->Underworld]]"
        },
        {
          "linkText": "HEAVY",
          "passageName": "Underworld",
          "original": "[[HEAVY->Underworld]]"
        },
        {
          "linkText": "TON",
          "passageName": "Sandstorm",
          "original": "[[TON->Sandstorm]]"
        }
      ],
      "hooks": [],
      "cleanText": "The sphinx peers deep into your eyes as if to study your very soul. \"What is heavy, but not backwards?\" You ponder your choices, what could it be? Perhaps its TON, LIGHT, or HEAVY. \"Choose wisely mortal, or you may find yourself in a realm most unpleasent."
    },
    {
      "name": "Sandstorm",
      "tags": "",
      "id": "12",
			"score":10,
      "text": "The sphinx is pleased with your response and permits you to pass. You continue over a large dune. At the top you see a violent sandstorm approaching. In your attempt to run, you trip and fall down the wrong side of the dune. You could HUNKER down to attempt to protect yourself or you could RUN.\n\n[[HUNKER->Underworld]] \n[[RUN->Cave]]",
      "links": [
        {
          "linkText": "HUNKER",
          "passageName": "Underworld",
          "original": "[[HUNKER->Underworld]]"
        },
        {
          "linkText": "RUN",
          "passageName": "Cave",
          "original": "[[RUN->Cave]]"
        }
      ],
      "hooks": [],
      "cleanText": "The sphinx is pleased with your response and permits you to pass. You continue over a large dune. At the top you see a violent sandstorm approaching. In your attempt to run, you trip and fall down the wrong side of the dune. You could HUNKER down to attempt to protect yourself or you could RUN."
    },
    {
      "name": "Cave",
      "tags": "",
      "id": "13",
			"score":10,
      "text": "You are extremely lucky to have found this cave to hide in. The storm rages on outside but is a mere breeze inside the cave. You hear chittering from inside the cave. You are not alone. All at once hundreds of beetles fly towards you. You could RETURN to the sandstorm or try to STOMP the beetles.\n\n[[RETURN->Sandstorm]] \n[[STOMP->Swarmed]]",
      "links": [
        {
          "linkText": "RETURN",
          "passageName": "Sandstorm",
          "original": "[[RETURN->Sandstorm]]"
        },
        {
          "linkText": "STOMP",
          "passageName": "Swarmed",
          "original": "[[STOMP->Swarmed]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are extremely lucky to have found this cave to hide in. The storm rages on outside but is a mere breeze inside the cave. You hear chittering from inside the cave. You are not alone. All at once hundreds of beetles fly towards you. You could RETURN to the sandstorm or try to STOMP the beetles."
    },
    {
      "name": "Swarmed",
      "tags": "",
      "id": "14",
			"score":10,
      "text": "The beetles overwhelm you. Now is a good time to SCREAM.\n\n[[SCREAM->Underworld]]",
      "links": [
        {
          "linkText": "SCREAM",
          "passageName": "Underworld",
          "original": "[[SCREAM->Underworld]]"
        }
      ],
      "hooks": [],
      "cleanText": "The beetles overwhelm you. Now is a good time to SCREAM."
    },
    {
      "name": "The Scales of Fate",
      "tags": "",
      "id": "15",
			"score":10,
      "text": "You decide to follow Anubis as he leads you to a great hall. Both sides are lined with giant men that Anubis explains are the judges and the head judge Osiris waits by the Scales of Fate. He holds in his left hand a feather. His right hand is empty. \"Give me your heart mortal.\" Do you GIVE him your heart or BEG for your life?\n\n[[GIVE->The Final Judgment]]\n[[BEG->Osiris]]",
      "links": [
        {
          "linkText": "GIVE",
          "passageName": "The Final Judgment",
          "original": "[[GIVE->The Final Judgment]]"
        },
        {
          "linkText": "BEG",
          "passageName": "Osiris",
          "original": "[[BEG->Osiris]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to follow Anubis as he leads you to a great hall. Both sides are lined with giant men that Anubis explains are the judges and the head judge Osiris waits by the Scales of Fate. He holds in his left hand a feather. His right hand is empty. \"Give me your heart mortal.\" Do you GIVE him your heart or BEG for your life?"
    },
    {
      "name": "The Final Judgment",
      "tags": "",
      "id": "16",
			"score":10,
      "text": "Osiris extracts your heart. It isn't beating, but you feel as though it being gone has no impact on your consciousness just yet. He places your heart on one side and the feather on the other. \"Answer these questions truthfully, or face Apophis.\" Will you ANSWER the questions or GIVE-UP.\n\n[[GIVE-UP->Apophis]]\n[[ANSWER->Question One]]",
      "links": [
        {
          "linkText": "GIVE-UP",
          "passageName": "Apophis",
          "original": "[[GIVE-UP->Apophis]]"
        },
        {
          "linkText": "ANSWER",
          "passageName": "Question One",
          "original": "[[ANSWER->Question One]]"
        }
      ],
      "hooks": [],
      "cleanText": "Osiris extracts your heart. It isn't beating, but you feel as though it being gone has no impact on your consciousness just yet. He places your heart on one side and the feather on the other. \"Answer these questions truthfully, or face Apophis.\" Will you ANSWER the questions or GIVE-UP."
    },
    {
      "name": "Osiris",
      "tags": "",
      "id": "17",
			"score":10,
      "text": "He laughs at you. You feel embarrassed and return to you feet. He holds out his hand once more. \"Give me your heart mortal.\" You may have no other choice but to GIVE Osiris your heart.\n\n[[GIVE->The Final Judgment]]",
      "links": [
        {
          "linkText": "GIVE",
          "passageName": "The Final Judgment",
          "original": "[[GIVE->The Final Judgment]]"
        }
      ],
      "hooks": [],
      "cleanText": "He laughs at you. You feel embarrassed and return to you feet. He holds out his hand once more. \"Give me your heart mortal.\" You may have no other choice but to GIVE Osiris your heart."
    },
    {
      "name": "Apophis",
      "tags": "",
      "id": "18",
			"score":10,
      "text": "\"You have been judged and found unworthy of paradise!\" The embodiment of chaos, Apophis, devours your being and you become part of the chaos itself. Do you want to play AGAIN?\n\n[[AGAIN->The Trident Paths]]",
      "links": [
        {
          "linkText": "AGAIN",
          "passageName": "The Trident Paths",
          "original": "[[AGAIN->The Trident Paths]]"
        }
      ],
      "hooks": [],
      "cleanText": "\"You have been judged and found unworthy of paradise!\" The embodiment of chaos, Apophis, devours your being and you become part of the chaos itself. Do you want to play AGAIN?"
    },
    {
      "name": "Question One",
      "tags": "",
      "id": "19",
			"score":10,
      "text": "\"You come across a man buried in sand, do you pass him by and LEAVE him or do you stop and HELP him?\"\n\n[[LEAVE->Apophis]] \n[[HELP->Question Two]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "Apophis",
          "original": "[[LEAVE->Apophis]]"
        },
        {
          "linkText": "HELP",
          "passageName": "Question Two",
          "original": "[[HELP->Question Two]]"
        }
      ],
      "hooks": [],
      "cleanText": "\"You come across a man buried in sand, do you pass him by and LEAVE him or do you stop and HELP him?\""
    },
    {
      "name": "Question Two",
      "tags": "",
      "id": "20",
			"score":10,
      "text": "\"You win a large sum of money. A dear friend falls terminally ill. With your funds, they will live. Do you KEEP the money for yourself or do you GIVE your friend the funds he needs to live?\"\n\n[[GIVE->Question Three]]\n[[KEEP->Apophis]]",
      "links": [
        {
          "linkText": "GIVE",
          "passageName": "Question Three",
          "original": "[[GIVE->Question Three]]"
        },
        {
          "linkText": "KEEP",
          "passageName": "Apophis",
          "original": "[[KEEP->Apophis]]"
        }
      ],
      "hooks": [],
      "cleanText": "\"You win a large sum of money. A dear friend falls terminally ill. With your funds, they will live. Do you KEEP the money for yourself or do you GIVE your friend the funds he needs to live?\""
    },
    {
      "name": "Question Three",
      "tags": "",
      "id": "21",
			"score":10,
      "text": "\"Answer this question and your fate is determined. The scales, as of now, are tipped in your favor. This is arguably the most important question in all of history. DOGS or CATS?\"\n\n[[DOGS->Paradise]]\n[[CATS->Apophis]]",
      "links": [
        {
          "linkText": "DOGS",
          "passageName": "Paradise",
          "original": "[[DOGS->Paradise]]"
        },
        {
          "linkText": "CATS",
          "passageName": "Apophis",
          "original": "[[CATS->Apophis]]"
        }
      ],
      "hooks": [],
      "cleanText": "\"Answer this question and your fate is determined. The scales, as of now, are tipped in your favor. This is arguably the most important question in all of history. DOGS or CATS?\""
    },
    {
      "name": "Paradise",
      "tags": "",
      "id": "22",
			"score":10,
      "text": "\"Your heart is pure and your disires kind. You may enjoy your afterlife in paradise. Go forth and enjoy your eternity.\" Osiris gives a warm smile and you are bathed in light. You find yourself feeling overwhelming happiness as your paradise awaits for you to explore it. Do you wish to play AGAIN?\n\n[[AGAIN->The Trident Paths]]",
      "links": [
        {
          "linkText": "AGAIN",
          "passageName": "The Trident Paths",
          "original": "[[AGAIN->The Trident Paths]]"
        }
      ],
      "hooks": [],
      "cleanText": "\"Your heart is pure and your disires kind. You may enjoy your afterlife in paradise. Go forth and enjoy your eternity.\" Osiris gives a warm smile and you are bathed in light. You find yourself feeling overwhelming happiness as your paradise awaits for you to explore it. Do you wish to play AGAIN?"
    }
  ]
}

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
		print("Moves: " + str(moves),"Score: " + str(score))
		print("You are at the " + str(current_location["name"]))
		print(current_location["cleanText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label

location_label = "The Trident Paths"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	moves += 1
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score = score + current_location["score"]
	render(current_location, score, moves)
	response = get_input()


print("Thanks for playing!")