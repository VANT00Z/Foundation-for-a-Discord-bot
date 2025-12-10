# Dear developer

This simple base for discord bot. In some cases discord.py doesnt work so check: Environment setup

# Environment setup:

1. Create environment. Press f1 and choose Create Environment. Than press Venv and 'Python...'.

2. Now you have environment, write in terminal: .venv/scripts/pip.exe install discord.py.

3. You installed discord.py, so now you can write code for your Discord-bot.

# How to create:

| Item   | Command |
|:------:| :------:|
| Bot    | bot = commands.Bot(command_prefix='YOUR_PREFIX', intents=intents) |
| Intents | intents = discord.Intents.default() |
| Bot command | @bot.command() |


# Dictionary:
* intents.guilds                        -     Events servers (guilds)

* intents.members                       -     Events members of server

* intents.moderation                    -     Moderation events (Bans, t.c)

* intents.emojis                        -     Events emojis and stickers

* intents.integrations                  -     Events integrations

* intents.webhooks                      -     Events webhooks

* intents.invites                       -     Events invites

* intents.voice_states                  -     States voices

* intents.presences                     -     Statuses and activities members

* intents.messages                      -     Messages in text channels

* intents.guild_messages                -     Messages on servers

* intents.dm_messages                   -     Messages in direct

* intents.message_content               -     Access to message content

* intents.reactions                     -     Reactions messages reactions

* intents.guild_reactions               -     Reactions on servers

* intents.dm_reactions                  -     Reactions in direct

* intents.typing                        -     Events messages sets

* intents.guild_typing                  -     Message set messages on servers

* intents.dm_typing                     -     Message set messages in direct

* intents.scheduled_events              -     Events

* intents.auto_moderation               -     Events auto-moderation

* intents.auto_moderation_configuration -     Configuration auto_moderation

* intents.auto_moderation_execution     -     Auto-moderation execution

## You can write: intents = discord.Intents.all() for give all intents to bot

|.fetch_user | Command to take info about user |

## user = await bot.fetch_user('USER_ID')
| Command              |    Action |
| user.id              | take ID |
| user.name            | Name of user |
| user.discriminator   | Tag (for example: 1234) |
| user.avatar.url      | URL of avatar |
| user.bot             | Return True if user is bot |
| user.created_at      | Account creation date |
| user.display_name    | Display name |
| user.mention         | Mention (@username) |