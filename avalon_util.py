import enum
import collections

class Role(enum.Enum):
    ASSASSIN = 7
    MORDRED = 6
    MORGANA = 5
    OBERON = 4
    MINION = 3
    MERLIN = 2
    PERCIVAL = 1
    SERVANT = 0

ROLE_STRINGS = ['Assassin',
                'Mordred',
                'Morgana',
                'Oberon',
                'Minion of Mordred',
                'Merlin',
                'Percival',
                'Loyal Servant of Arthur']

STR_2_ROLE = dict(zip(ROLE_STRINGS, list(Role)))

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
