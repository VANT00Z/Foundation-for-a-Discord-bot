'''imports'''
import discord #<- import library discord
from discord.ext import commands #<- import commands to use


'''settings for bot'''
intents = discord.Intents.all() #<- granting access to intents (can use Intents.default())
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents) #<- Setting the prefix '!' (it can be anything)


''' events '''

''' when the bot starts '''
@bot.event
async def on_ready():
    print(f'Bot {bot.user} is ready')   # the following is output to the terminal: Bot [name of your bot] is ready

''' if user send unknown command '''
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Unknown command') #<- bot say that


''' commands '''

''' say hello '''
@bot.command()
async def hello(ctx):
    await ctx.send('Hello World!')

''' "echo" command'''
@bot.command()
async def echo(ctx, message):   #<- there takes the message as argument
    await ctx.send(message)   #then send it

''' "tag" command'''
@bot.command()
async def tag(ctx):
    await ctx.send(ctx.author.mention)
    
''' command send to direct messages'''
@bot.command()
async def direct(ctx, user_id): #<- there it take user id as argument
    id = await bot.fetch_user(user_id) #<- here are a few ways to translate this, depending on the context
    
    await id.send('I can write in direct!')
    
'''mention user'''
@bot.command()
async def ment(ctx):
    ctx.send(f'{ctx.author.mention}')

'''bot run'''
bot.run('YOUR_BOT_TOKEN') #<- change it to your bot token


'''P.S.'''
#   more on GitHub
#   link to Git: https://github.com/VANT00Z (or @VANT00Z)
#   dictionary with commands and explains in read-me.txt
#   join to my discord server: https://discord.gg/3cTGprws
