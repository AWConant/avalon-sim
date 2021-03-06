import sys
import random

import avalon_util

def main():
    # Read player info from stdin.
    player_count = int(input('How many players? '))
    if not (5 <= player_count <= 10):
        print('Number of players must be at least 5 and no more than 10.')
        sys.exit()

    print('Please enter %d player names below.' % player_count)
    player_names = [input('Enter a player name: ') for _ in range(player_count)]

    print('\nPlease enter %d role names; the valid options are listed below.' % player_count)
    for role_string in avalon_util.ROLE_STRINGS:
        print(role_string)
    selected_roles = [input('Enter a role name: ') for _ in range(player_count)]

    # Map role input to enums and randomize the order.
    roles = [lookup_role_enum(role_string) for role_string in selected_roles]
    random.shuffle(roles)
    
    # Construct players.
    players = [Player(name, role, (set(roles) & avalon_util.KNOWN_ROLES[role]))
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
