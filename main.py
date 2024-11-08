import discord
from discord.ext import commands
import edu_ai, prompts, io

#测试用
bot = 'your token'

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

thread_dict = {}

# client = commands.Bot(command_prefix='?', intents=intents, proxy='http://localhost:1080')
client = commands.Bot(command_prefix='?', intents=intents)


class Analogies_Modal(discord.ui.Modal, title = 'In-Depth Study!'):
    inputs = discord.ui.TextInput(label='Type your keywords!', placeholder='Type your keywords!', style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer()
        submitted = self.inputs.value
        str_to_ai = prompts.analogies(submitted)
        dc_thread_id = interaction.channel_id
        ai_res = edu_ai.add_message_and_running(user_inputs = str_to_ai, thread_id = thread_dict[str(dc_thread_id)])
        await interaction.message.reply(ai_res)

class Roleplay_Modal(discord.ui.Modal, title = 'In-Depth Study!'):
    inputs = discord.ui.TextInput(label='Type your keywords!', placeholder='Type your keywords!', style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer()
        submitted = self.inputs.value
        str_to_ai = prompts.roleplay(submitted)
        dc_thread_id = interaction.channel_id
        ai_res = edu_ai.add_message_and_running(user_inputs = str_to_ai, thread_id = thread_dict[str(dc_thread_id)])
        await interaction.message.reply(ai_res)

class Journey_Modal(discord.ui.Modal, title = 'In-Depth Study!'):
    inputs = discord.ui.TextInput(label='Type your keywords!', placeholder='Type your keywords!', style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer()
        submitted = self.inputs.value
        str_to_ai = prompts.journey(submitted)
        dc_thread_id = interaction.channel_id
        ai_res = edu_ai.add_message_and_running(user_inputs = str_to_ai, thread_id = thread_dict[str(dc_thread_id)])
        await interaction.message.reply(ai_res)

class Scratic_Modal(discord.ui.Modal, title = 'In-Depth Study!'):
    inputs = discord.ui.TextInput(label='Type your keywords!', placeholder='Type your keywords!', style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer()
        submitted = self.inputs.value
        str_to_ai = prompts.scratic(submitted)
        dc_thread_id = interaction.channel_id
        ai_res = edu_ai.add_message_and_running(user_inputs = str_to_ai, thread_id = thread_dict[str(dc_thread_id)])
        await interaction.message.reply(ai_res)

class Retrospect_Modal(discord.ui.Modal, title = 'In-Depth Study!'):
    inputs = discord.ui.TextInput(label='Type your keywords!', placeholder='Type your keywords!', style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer()
        submitted = self.inputs.value
        str_to_ai = prompts.retrospect(submitted)
        dc_thread_id = interaction.channel_id
        ai_res = edu_ai.add_message_and_running(user_inputs = str_to_ai, thread_id = thread_dict[str(dc_thread_id)])
        await interaction.message.reply(ai_res)

class Imagining_Modal(discord.ui.Modal, title = 'In-Depth Study!'):
    inputs = discord.ui.TextInput(label='Type your keywords!', placeholder='Type your keywords!', style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer()
        submitted = self.inputs.value
        str_to_ai = prompts.imagining(submitted)
        dc_thread_id = interaction.channel_id
        ai_res = edu_ai.add_message_and_running(user_inputs = str_to_ai, thread_id = thread_dict[str(dc_thread_id)])
        await interaction.message.reply(ai_res)

class Basic_Modal(discord.ui.Modal, title = 'Basic Communication'):
    inputs = discord.ui.TextInput(label='Type your keywords!', placeholder='Type your keywords!', style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer()
        submitted = self.inputs.value
        str_to_ai = prompts.basic(submitted)
        dc_thread_id = interaction.channel_id
        ai_res = edu_ai.add_message_and_running(user_inputs = str_to_ai, thread_id = thread_dict[str(dc_thread_id)])
        await interaction.message.reply(ai_res)

class Judge_Modal(discord.ui.Modal, title = 'Content rRelevance Assessment'):
    inputs = discord.ui.TextInput(label='Type your keywords!', placeholder='Type your keywords!', style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer()
        submitted = self.inputs.value
        str_to_ai = prompts.judge(submitted)
        dc_thread_id = interaction.channel_id
        ai_res = edu_ai.add_message_and_running(user_inputs = str_to_ai, thread_id = thread_dict[str(dc_thread_id)])
        await interaction.message.reply(ai_res)
# --------------------------------------------------------------------------------------------------------------

class Analogies(discord.ui.Button):
    def __init__(self):
        super().__init__()
        self.style=discord.ButtonStyle.primary
        self.label='Analogies and Metaphors'
        self.row = 1

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(Analogies_Modal())

class Roleplay(discord.ui.Button):
    def __init__(self):
        super().__init__()
        self.style=discord.ButtonStyle.primary
        self.label='Story Roleplay'
        self.row = 1
        
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(Roleplay_Modal())

class Journey(discord.ui.Button):
    def __init__(self):
        super().__init__()
        self.style=discord.ButtonStyle.primary
        self.label='Story Journey'
        self.row = 1
        
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(Journey_Modal())

class Scratic(discord.ui.Button):
    def __init__(self):
        super().__init__()
        self.style=discord.ButtonStyle.primary
        self.label='Scratic'
        self.row = 2

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(Scratic_Modal())

class Retrospect(discord.ui.Button):
    def __init__(self):
        super().__init__()
        self.style=discord.ButtonStyle.primary
        self.label='Retrospect'
        self.row = 2
        
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(Retrospect_Modal())

class Imagining(discord.ui.Button):
    def __init__(self):
        super().__init__()
        self.style=discord.ButtonStyle.primary
        self.label='Imagining'
        self.row = 2
        
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(Imagining_Modal())

class Basic(discord.ui.Button):
    def __init__(self):
        super().__init__()
        self.style=discord.ButtonStyle.secondary
        self.label='Basic'
        self.row = 0
        
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(Basic_Modal())

class Judge(discord.ui.Button):
    def __init__(self):
        super().__init__()
        self.style=discord.ButtonStyle.secondary
        self.label='Judge'
        self.row = 0
        
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(Judge_Modal())


class MyView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Basic())
        self.add_item(Judge())
        self.add_item(Analogies())
        self.add_item(Roleplay())
        self.add_item(Journey())
        self.add_item(Scratic())
        self.add_item(Retrospect())
        self.add_item(Imagining())


@client.event
async def on_ready():
    print('bot is ready')
    
#  https://discordpy.readthedocs.io/en/latest/faq.html#why-does-on-message-make-my-commands-stop-working
@client.event
async def on_message(message):

    # ?start只能在公共频道调用
    if str(message.channel.id) not in list(thread_dict.keys()) and message.content == '?start':
        await client.process_commands(message)
    
    # 对thread内的消息进行处理
    # 注意类型，这里是判断str是否在另一个基本元素为str的list中
    elif str(message.channel.id) in list(thread_dict.keys()) and message.author.bot == False and message.content not in ['?start', '?learn', '?log']:
        try:
            ai_res = edu_ai.add_message_and_running(
                user_inputs = message.content, 
                thread_id = thread_dict[str(message.channel.id)]
                )
            await message.reply(ai_res)

        except Exception:
            await message.reply(f'{Exception}')

    # ?learn只能在thread中调用
    elif str(message.channel.id) in list(thread_dict.keys()) and message.content == '?learn':
        await client.process_commands(message)
    
    # ?log只能在thread中调用
    elif str(message.channel.id) in list(thread_dict.keys()) and message.content == '?log':
        await client.process_commands(message)

    else:
        return


@client.command()
async def learn(ctx):
    await ctx.send(view = MyView())


@client.command()
async def log(ctx):
    # dc_thread -> gpt_thread -> messsage
    dc_thread_id = ctx.message.channel.id
    gpt_thread_id = thread_dict[str(dc_thread_id)]
    messages_list = edu_ai.client.beta.threads.messages.list(thread_id = gpt_thread_id)

    my_text = str(messages_list)
    buffer = io.BytesIO(my_text.encode("utf8"))  # change encoding as necessary

    await ctx.send(file=discord.File(fp = buffer, filename = 'ThreadHistory.txt'))


@client.command()
async def start(ctx):
    dc_thread = await ctx.message.channel.create_thread(name = 'AI Communicating')
    
    await dc_thread.add_user(ctx.author)

    my = await client.fetch_user(803664702717689907)
    await dc_thread.add_user(my)

    await dc_thread.send(content = 'Welcome to the learning journey of Information Technology Professional Ethics. How may I assist you?')
    
    gpt_thread_id = edu_ai.create_thread() #用户调用命令后，创建GPT的thread
    
    # thread_list.append(dc_thread.id)
    thread_dict[f'{dc_thread.id}'] = gpt_thread_id #str => int

client.run(bot)