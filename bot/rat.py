import discord
from discord import app_commands
from discord.ui import Button, View, Select
from discord.utils import get
from discord import Colour
from Log import log
import components
from components import available_servers,pickup,jobs,departments,grades,get_ids
NCUE = 764126539041734679
token="MTAyMDM1OTg0NTU5NTA1NDA4MA.G_xkZr._TOqJLn7iTsN3FF9Y1AuGLg1uIBSArwLAKkSrM"
guild_list:list[discord.Object] = []


GIDS = []

async def initialize_roles(guild_id,selections:list[discord.SelectOption],colors:list[discord.Colour]):
    guild = client.get_guild(guild_id)
    for n in range(len(selections)):
        if selections[n].emoji == None : val = selections[n].label
        else: val = (selections[n].emoji).name+"."+selections[n].label
        if not get(guild.roles,name=val): 
            await guild.create_role(name=val,hoist=True,colour=colors[n])
history = log()
class bot_client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
        global guild_obj_list
        guild_obj_list = [
            discord.Object(id=1003642488826900551),
            discord.Object(id=1058639961500426320)
        ]
    async def on_ready(self):
        global history,guild_list,guild_obj_list2,GIDS
        guild_obj_list2 = [str(i.name)+" , "+str(i.id) for i in client.guilds]
        await self.wait_until_ready()
        guild_list = [g for g in client.guilds]
        guild_list = pickup(guild_list,history)
        for i in guild_list: GIDS.append(i.id)
        
        if not self.synced:
            for guild in guild_list:
                history.println("Synchronizing "+guild.name+".....")
                await tree.sync(guild=discord.Object(id=guild.id))
            self.synced = True
        for i in guild_list:
            career_colors = [Colour.dark_gold(),Colour.green(),Colour.dark_grey(),Colour.from_rgb(139,69,19)]
            if(i.id == NCUE):
                await initialize_roles(guild_id=i.id,selections=departments+grades,colors=[Colour.blue() for _ in range(len(departments+grades))])
            else:
                await initialize_roles(guild_id=i.id,selections=jobs,colors=career_colors)
        
        history.println("GUILDS:")
        for i in guild_list:
            history.println(i.name)
        history.println("logged in as " + self.user.display_name)
        # print(history.show())

client = bot_client()
tree = app_commands.CommandTree(client)



class department_select(Select):
    def __init__(self):
        super().__init__(
            placeholder ="??????????????????",
            min_values=1,
            max_values=1,
            options=departments
        )
    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        guild = interaction.guild
        await interaction.response.send_message(f"{user.name} ????????? {self.values[0]}",ephemeral=True)
        for i in self.options:
            current =  get(guild.roles, name=i.emoji.name+"."+i.label)
            if current.name.split(".")[1] == self.values[0]: await user.add_roles(current)
            else:  await user.remove_roles(current)

class grade_select(Select):
    def __init__(self):
        super().__init__(
            placeholder = "??????????????????",
            min_values=1,
            max_values=1,
            options=grades
        )
    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        guild = interaction.guild
        await interaction.response.send_message(f"{user.name} ????????? {self.values[0]}",ephemeral=True)
        for i in self.options:
            current =  get(guild.roles, name=i.label)
            if current.name==self.values[0]: await user.add_roles(current)
            else:  await user.remove_roles(current)

class yes_no_view(View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Button(style=discord.ButtonStyle.green,emoji="???"))
        self.add_item(Button(style=discord.ButtonStyle.red,emoji="???"))

class select_view(View):
    def __init__(self,item,timeout=180):
        super().__init__(timeout=timeout)
        self.add_item(item)

@tree.command(name="??????????????????????????????",description="??????????????????????????????",guilds=guild_obj_list)
async def self(i:discord.Interaction):
    history.println("<"+i.user.name+"> send a command "+self.name)
    guilds = i.client.guilds
    len(guilds)
    show = "??????\n"
    for guild in guilds: show+="["+str(guild.id)+"] "+guild.name+"\n"
    await i.response.send_message(f"{show}")
    # print(show)

@tree.command(name="?????????????????????",description="???????????????????????????????????????",guilds=guild_obj_list)
async def self(i:discord.Interaction):
    history.println("<"+i.user.name+"> send a command "+self.name)
    await i.response.send_message(f"{history.show()}")

@tree.command(name="close",description="turn off this bot globally",guilds=guild_obj_list)
async def self(interaction:discord.Interaction,password:str):
    if password=="ratoff":
        await interaction.response.send_message(f"turing off rat .....")
        await client.close()

@tree.command(name="??????",description="??????",guilds=guild_obj_list)
async def self(interaction:discord.Interaction):
    user = interaction.user
    with open("database/works.txt",'a') as work_file:
            work_file.write(f"work-{user.name}-100\n")
    await interaction.response.send_message(f"work,{user.name},100\n",ephemeral=True)

@tree.command(name="?????????",description="test of selector",guilds=guild_obj_list)
async def self(interaction:discord.Interaction):
    await interaction.response.send_message(f"select your job",view=select_view(components.job_select()),ephemeral=True)

@tree.command(name="????????????",description="??????????????????????????????????????????",guilds=guild_obj_list)
async def self(interaction:discord.Interaction):
    await interaction.response.send_message(f"??????????????????",view=select_view(department_select()),ephemeral=False)

@tree.command(name="????????????",description="??????????????????????????????????????????",guilds=guild_obj_list)
async def self(interaction:discord.Interaction):
    await interaction.response.send_message(f"??????????????????",view=select_view(grade_select()),ephemeral=False)

client.run(token)
