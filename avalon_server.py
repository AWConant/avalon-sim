import enum
import sys
import random
import collections

class Role(enum.Enum):
    ASSASSIN = 7
    MORDRED = 6
    MORGANA = 5
    MINION = 4
    OBERON = 3
    MERLIN = 2
    PERCIVAL = 1
    SERVANT = 0

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

QUEST_SIZES = {5:  [2, 3, 2, 3, 3],
               6:  [2, 3, 4, 3, 4],
               7:  [2, 3, 3, 4, 4],
               8:  [3, 4, 4, 5, 5],
               9:  [3, 4, 4, 5, 5],
               10: [3, 4, 4, 5, 5],
               }
                  
Player = collections.namedtuple('Player', ['name', 'role', 'known'])

def lookup_role_enum(s):
    try:
        return STR_2_ROLE[s]
    except KeyError:
        print("'%s' is not a valid role." % s)
        sys.exit()

def main():
    # Read player info from stdin.
    player_count = int(input('How many players? '))
    if not (5 <= player_count <= 10):
        print('Number of players must be at least 5 and no more than 10.')
        sys.exit()

    print('Please enter %d player names below.' % player_count)
    player_names = [input('Enter a player name: ') for _ in range(player_count)]

    print('\nPlease enter %d role names; the valid options are listed below.' % player_count)
    for name in STR_2_ROLE.keys():
        print(name)
    selected_roles = [input('Enter a role name: ') for _ in range(player_count)]

    # Map role input to enums and randomize the order.
    roles = [lookup_role_enum(role_string) for role_string in selected_roles]
    random.shuffle(roles)
    
    # Construct players.
    players = [Player(name, role, (set(roles) & KNOWN_ROLES[role]))
               for name, role
               in zip(player_names, roles)]

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
