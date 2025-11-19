<html>
<body>
  <h1>Dear developer</h1>
  <h3>This simple base for discord bot. In some cases <code>discord.py</code> doesnt work so check: <code>Environment setup</code></h3>
  <h1>Environment setup:</h1>
  <ol>
    <h3><li>
      Create environment. Press f1 and choose <code>Create Environment</code>. Than press <code>Venv</code>  and 'Python...'.
    </li></h3>
    <h3><li>
      Now you have environment, write in terminal: <code>.venv/scripts/pip.exe install discord.py</code>.
    </li></h3>
    <h3><li>
       You installed discord.py, so now you can write code for your Discord-bot
    </li></h3>
  </ol>

<h1>How to create:</h1>

<p><code>Bot                                   -     bot = commands.Bot(command_prefix='YOUR_PREFIX', intents=intents)</code></p>
<p><code>Intents                               -     intents = discord.Intents.default()</code></p>
<p><code>bot command                           -     @bot.command()</code></p>


<h1>Dictionary:</h1>

<p><code>intents.guilds                        -     Events servers (guilds)</code></p>
<p><code>intents.members                       -     Events members of server</code></p>
<p><code>intents.moderation                    -     Moderation events (Bans, t.c)</code></p>
<p><code>intents.emojis                        -     Events emojis and stickers</code></p>
<p><code>intents.integrations                  -     Events integrations</code></p>
<p><code>intents.webhooks                      -     Events webhooks</code></p>
<p><code>intents.invites                       -     Events invites</code></p>
<p><code>intents.voice_states                  -     States voices</code></p>
<p><code>intents.presences                     -     Statuses and activities members</code></p>
<p><code>intents.messages                      -     Messages in text channels</code></p>
<p><code>intents.guild_messages                -     Messages on servers</code></p>
<p><code>intents.dm_messages                   -     Messages in direct</code></p>
<p><code>intents.message_content               -     Access to message content</code></p>
<p><code>intents.reactions                     -     Reactions messages reactions</code></p>
<p><code>intents.guild_reactions               -     Reactions on servers</code></p>
<p><code>intents.dm_reactions                  -     Reactions in direct</code></p>
<p><code>intents.typing                        -     Events messages sets</code></p>
<p><code>intents.guild_typing                  -     Message set messages on servers</code></p>
<p><code>intents.dm_typing                     -     Message set messages in direct</code></p>
<p><code>intents.scheduled_events              -     Events</code></p>
<p><code>intents.auto_moderation               -     Events auto-moderation</code></p>
<p><code>intents.auto_moderation_configuration -     Configuration auto_moderation</code></p>
<p><code>intents.auto_moderation_execution     -     Auto-moderation execution</code></p>

<h2>*You can write: intents = discord.Intents.all() for give all intents to bot</h2>

<p><code>.fetch_user                           -     Command to take info about user</code></p>

<h2>user = await bot.fetch_user('USER_ID')</h2>

<p><code>user.id                               -     take ID</code></p>
<p><code>user.name                             -     Name of user</code></p>
<p><code>user.discriminator                    -     Tag (for example: 1234)</code></p>
<p><code>user.avatar.url                       -     URL of avatar</code></p>
<p><code>user.bot                              -     Return True if user is bot</code></p>
<p><code>user.created_at                       -     Account creation date</code></p>
<p><code>user.display_name                     -     Display name</code></p>
<p><code>user.mention                          -     Mention (@username)</code></p>
</body>
</html>
