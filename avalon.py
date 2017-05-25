import enum
import sys
import random
import collections

class Role(enum.Enum):
    ASSASSIN = 'Assassin'
    MORDRED = 'Mordred'
    MORGANA = 'Morgana'
    OBERON = 'Oberon'
    MINION = 'Minion of Mordred'
    MERLIN = 'Merlin'
    PERCIVAL = 'Percival'
    SERVANT = 'Loyal Servant of Arthur'

STR_2_ROLE = {
    'Assassin': Role.ASSASSIN,
    'Mordred': Role.MORDRED, 
    'Morgana': Role.MORGANA, 
    'Oberon': Role.OBERON, 
    'Minion of Mordred': Role.MINION, 
    'Merlin': Role.MERLIN, 
    'Percival': Role.PERCIVAL, 
    'Loyal Servant of Arthur': Role.SERVANT, 
    }

EVIL_ROLES = {Role.MORDRED, Role.MORGANA, Role.MINION, Role.ASSASSIN}
GOOD_ROLES = {Role.MERLIN, Role.PERCIVAL, Role.SERVANT}

KNOWN_ROLES = collections.defaultdict(set,
                  ((Role.ASSASSIN, EVIL_ROLES - {Role.ASSASSIN}),
                   (Role.MORDRED, EVIL_ROLES - {Role.MORDRED}),
                   (Role.MORGANA, EVIL_ROLES - {Role.MORGANA}),
                   (Role.MINION, EVIL_ROLES - {Role.MINION}),
                   (Role.MERLIN, EVIL_ROLES - {Role.MORDRED}),
                  )
              )

# TODO: Provide ordering for assassination privilege

# TODO: Map player_count to quest sizes
                  
Player = collections.namedtuple('Player', ['name', 'role', 'known'])

def main():
    # Read player info from stdin.
    player_count = int(input())

    # TODO: Verify number of players.

    player_names = [input() for _ in range(player_count)]
    selected_roles = [input() for _ in range(player_count)]

    # Map role input to enums and randomize the order.
    # TODO: Fail gracefully if any role is invalid.
    roles = [STR2ROLE[role] for role in selected_roles]
    random.shuffle(roles)

    # TODO: Verify that there is Merlin
    
    # Construct players.
    players = [Player(name, role, set(roles) & KNOWN_ROLES[role]) for name, role in zip(player_names, roles)]

    # Pick a random index for the player who is to be the first leader.
    leader_idx = random.randrange(player_count)

    quests_passed = quests_failed = 0
    teams_rejected = 0
    while quests_passed < 3 and quests_failed < 3 and teams_rejected < 5: # TODO: iterate over quest sizes instead
        leader = players[leader_idx]
        # deliberate about team comp
        # leader chooses comp
        # vote on comp
        # if fail, try again and increment teams_rejected
        # if teams_rejected > 5, evil wins
        # players on quest choose pass/fail
        # reveal the voting results

        # Get index of next leader in players.
        leader_idx = (leader_idx + 1) % player_count

    # if quests_passed == 3, evil players deliberate about who to assassinate
    #   evil player with assassination privilege chooses a player
    #   if that player is merlin, evil wins
    # if quests_failed == 3, evil wins
    # otherwise, good wins
    


if __name__ == '__main__':
    main()
