import discord
from discord.ui import Select
from discord import SelectOption
from Log import log

jobs = [
    discord.SelectOption(label="miner",emoji="⛏️",description="a career that can get lot of jeweris"),
    discord.SelectOption(label="farmer",emoji="🥦",description="a career that can grow foods"),
    discord.SelectOption(label="smith",emoji="⚒️",description="a career that can make tools and weapons"),
    discord.SelectOption(label="hunter",emoji="🏹",description="a career that can get meats from nature")
]
departments = [
    discord.SelectOption(label="資工系",emoji="👓",description="資訊工程學系"),
    discord.SelectOption(label="資管系",emoji="🔐",description="資訊管理學系"),
    discord.SelectOption(label="電機系",emoji="🪛",description="電機工程學系"),
    discord.SelectOption(label="機電系",emoji="⚙️",description="機電工程學系")
]
grades = [discord.SelectOption(label=str(i)) for i in range(109,115)]

available_servers = ['彰化師範大學','無名氏','三隻狗','Yun 的伺服器']

class slection(Select):
    def __init__(self, *, custom_id: str = "job_selection", placeholder:str = "select your job", min_values: int = 1, max_values: int = 1, options: list[SelectOption] = ..., disabled: bool = False, row: int = None) -> None:
        super().__init__(custom_id=custom_id, placeholder=placeholder, min_values=min_values, max_values=max_values,options=options, disabled=disabled, row=row)


def pickup(guild_list:list,log:log):
    temp = []
    for g in guild_list:
            if g.name in available_servers:
                temp.append(g)
                log.println("🟢  " + g.name)
            else:
                log.println("🔴  " + g.name)
    return temp
def get_ids(guild_list:list):
    temp = []
    for guild in guild_list:
        temp.append(guild.id)
    return temp

class job_select(Select):
    def __init__(self):
        super().__init__(
            placeholder ="select your job",
            min_values=1,
            max_values=1,
            options=jobs
        )
    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        guild = interaction.guild
        ########################################################################
        def add_userdata(add):
            out = []
            lst = [line.strip('\n').split(" ") for line in open('database/jobs.txt').readlines()]
            for i in lst:
                cnt = 0
                #把檔案重複名字更新只留最後一個
                for j in out:
                    if i[0]==j[0]:
                        j[1]=i[1]
                    else:
                        cnt+=1
                if cnt == len(out):
                    out.append(i)
            #如果新加入的user名字存在在檔案中 -> 更新檔案
            cnt = 0
            for i in out:
                if add[0]==i[0]:
                    i[1]=add[1]
                else:
                    cnt += 1
            if cnt == len(out):
                out.append(add)
            with open('database/jobs.txt', 'w') as f:
                for i in out:
                    f.write(str(i[0])+" "+str(i[1])+"\n")
        ########################################################################
        add_userdata([str(user.name),str(self.values[0])])
        history.println(f"{user.name} select {self.values[0]} as job")
        await interaction.response.send_message(f"{user.name} select {self.values[0]} as job",ephemeral=True)
        for i in self.options:
            current =  get(guild.roles, name=i.emoji.name+"."+i.label)
            if current.name.split(".")[1] == self.values[0]: await user.add_roles(current)
            else:  await user.remove_roles(current)