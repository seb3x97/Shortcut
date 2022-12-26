#---------- Json Structure ----------#

#-- Global Sample --#
"""
[
    {:"Command Sample"},
    {:"Command Sample"},
    ...
]
"""

#-- Command Sample --#
"""
{
    "name": "Test",
    "shortcut": [162, 160, 76],
    "actions": [
        {
            "class": "mouse_move",
            "args": {"dx": 100, "dy": 200}
        }
    ]
}
"""

#---------- Noms des données ----------#

__COMMAND_NAME = 'name'
__COMMAND_SHORTCUT = 'shortcut'
__COMMAND_ACTIONS = 'actions'
#
__COMMAND_ACTION_CLASS = 'class'
__COMMAND_ACTION_ARGS = 'args'

#---------- Lambda Expressions ----------#

# -- Commande -- #
get_command_name = lambda command: command[__COMMAND_NAME]
get_command_shortcut = lambda command: tuple(command[__COMMAND_SHORTCUT])
get_command_actions = lambda command: command[__COMMAND_ACTIONS]
#
get_command_action_class = lambda action: action[__COMMAND_ACTION_CLASS]
get_command_action_args = lambda action: action[__COMMAND_ACTION_ARGS]