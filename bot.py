from urllib import request
import discord
from discord.ext import commands, tasks
from discord import app_commands
from dotenv import load_dotenv
import os

# Carregar as variáveis do .env
load_dotenv()

# Obter os valores das variáveis de ambiente
TOKEN = os.getenv('DISCORD_TOKEN')
API_KEY = os.getenv('FORTNITE_API_KEY')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

# Inicializando o bot com suporte a comandos de barra
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Função para pegar informações da loja do Fortnite
def get_fortnite_shop():
    url = "https://fortniteapi.io/shop"
    headers = {"Authorization": API_KEY}
    req = request.Request(url, headers=headers)
    with request.urlopen(req) as response:
        if response.status == 200:
            data = response.read().decode("utf-8")
            return data  # Processar o JSON aqui conforme necessário
        else:
            return None

# Comando de barra para redirecionar para o site da Epic Games
@bot.tree.command(name="epic", description="Redireciona para o site da Epic Games")
async def epic(interaction: discord.Interaction):
    await interaction.response.send_message("Clique aqui para visitar o site da Epic Games: [Epic Games](https://www.epicgames.com/)")

# Comando de barra para redirecionar para a loja do Fortnite
@bot.tree.command(name="loja", description="Redireciona para a loja do Fortnite")
async def loja(interaction: discord.Interaction):
    await interaction.response.send_message("Clique aqui para visitar a loja do Fortnite: [Loja Fortnite](https://www.epicgames.com/fortnite/pt-BR/shop)")

# Comando para enviar a loja manualmente
@bot.command()
async def loja_manual(ctx):
    items = get_fortnite_shop()
    if items:
        shop_message = "🛒 **Loja do Fortnite** 🛒\n\n"
        # Aqui você deve processar o `items` de acordo com a estrutura do JSON retornado pela API
        await ctx.send(shop_message)
    else:
        await ctx.send("Não foi possível obter os dados da loja do Fortnite.")

# Tarefa periódica para atualizar a loja no canal específico
@tasks.loop(hours=1)  # Atualiza a cada 1 hora
async def update_shop():
    channel = bot.get_channel(CHANNEL_ID)
    items = get_fortnite_shop()
    if items:
        shop_message = "🛒 **Loja do Fortnite** 🛒\n\n"
        # Aqui você deve processar o `items` de acordo com a estrutura do JSON retornado pela API
        await channel.send(shop_message)
    else:
        await channel.send("Não foi possível obter os dados da loja do Fortnite.")

# Evento para iniciar o bot
@bot.event
async def on_ready():
    print(f'Bot {bot.user} está online!')
    await bot.tree.sync()  # Sincroniza os comandos de barra
    update_shop.start()  # Inicia a tarefa periódica quando o bot estiver online

# Executando o bot
bot.run(TOKEN)


# Carregar as variáveis do .env
load_dotenv()

# Obter os valores das variáveis de ambiente
TOKEN = os.getenv('DISCORD_TOKEN')
API_KEY = os.getenv('FORTNITE_API_KEY')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

# Inicializando o bot com suporte a comandos de barra
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Função para pegar informações da loja do Fortnite
def get_fortnite_shop():
    url = "https://fortniteapi.io/shop"
    headers = {"Authorization": API_KEY}
    response = request.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['items']
    else:
        return None

# Comando de barra para enviar o link da Epic Games (corrigido para minúsculas)
@bot.tree.command(name="epic", description="Link para o site da Epic Games")
async def epic(interaction: discord.Interaction):
    await interaction.response.send_message("Visite o site da Epic Games: [Epic Games](https://www.epicgames.com/)")

# Comando de barra para enviar o link da loja do Fortnite (corrigido para minúsculas)
@bot.tree.command(name="loja", description="Link para a loja do Fortnite")
async def loja(interaction: discord.Interaction):
    await interaction.response.send_message("Visite a loja do Fortnite: [Loja Fortnite](https://www.epicgames.com/fortnite/pt-BR/shop)")

# Comando para enviar a loja manualmente
@bot.command()
async def loja_manual(ctx):
    items = get_fortnite_shop()
    if items:
        shop_message = "🛒 **Loja do Fortnite** 🛒\n\n"
        for item in items:
            shop_message += f"{item['name']} - {item['price']} V-Bucks\n"
        await ctx.send(shop_message)
    else:
        await ctx.send("Não foi possível obter os dados da loja do Fortnite.")

# Tarefa periódica para atualizar a loja no canal específico
@tasks.loop(hours=1)  # Atualiza a cada 1 hora
async def update_shop():
    channel = bot.get_channel(CHANNEL_ID)
    items = get_fortnite_shop()
    if items:
        shop_message = "🛒 **Loja do Fortnite** 🛒\n\n"
        for item in items:
            shop_message += f"{item['name']} - {item['price']} V-Bucks\n"
        await channel.send(shop_message)
    else:
        await channel.send("Não foi possível obter os dados da loja do Fortnite.")

# Evento para iniciar o bot
@bot.event
async def on_ready():
    print(f'Bot {bot.user} está online!')
    await bot.tree.sync()  # Sincroniza os comandos de barra
    update_shop.start()  # Inicia a tarefa periódica quando o bot estiver online

# Executando o bot
bot.run(TOKEN)


# Carregar as variáveis do .env
load_dotenv()

# Obter os valores das variáveis de ambiente
TOKEN = os.getenv('DISCORD_TOKEN')
API_KEY = os.getenv('FORTNITE_API_KEY')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

# Inicializando o bot com suporte a comandos de barra
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Função para pegar informações da loja do Fortnite
def get_fortnite_shop():
    url = "https://fortniteapi.io/shop"
    headers = {"Authorization": API_KEY}
    response = request.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['items']
    else:
        return None

# Comando de barra para enviar o link da Epic Games (corrigido para minúsculas)
@bot.tree.command(name="epic", description="Link para o site da Epic Games")
async def epic(interaction: discord.Interaction):
    await interaction.response.send_message("Visite o site da Epic Games: [Epic Games](https://store.epicgames.com/pt-BR/)")

# Comando de barra para enviar o link da loja do Fortnite (corrigido para minúsculas)
@bot.tree.command(name="loja", description="Link para a loja do Fortnite")
async def loja(interaction: discord.Interaction):
    await interaction.response.send_message("Visite a loja do Fortnite: [Loja Fortnite](fortnite.com/item-shop?lang=pt-BRc)")

# Comando para enviar a loja manualmente
@bot.command()
async def loja_manual(ctx):
    items = get_fortnite_shop()
    if items:
        shop_message = "🛒 **Loja do Fortnite** 🛒\n\n"
        for item in items:
            shop_message += f"{item['name']} - {item['price']} V-Bucks\n"
        await ctx.send(shop_message)
    else:
        await ctx.send("Não foi possível obter os dados da loja do Fortnite.")

# Tarefa periódica para atualizar a loja no canal específico
@tasks.loop(hours=1)  # Atualiza a cada 1 hora
async def update_shop():
    channel = bot.get_channel(CHANNEL_ID)
    items = get_fortnite_shop()
    if items:
        shop_message = "🛒 **Loja do Fortnite** 🛒\n\n"
        for item in items:
            shop_message += f"{item['name']} - {item['price']} V-Bucks\n"
        await channel.send(shop_message)
    else:
        await channel.send("Não foi possível obter os dados da loja do Fortnite.")

# Evento para iniciar o bot
@bot.event
async def on_ready():
    print(f'Bot {bot.user} está online!')
    await bot.tree.sync()  # Sincroniza os comandos de barra
    update_shop.start()  # Inicia a tarefa periódica quando o bot estiver online

# Executando o bot
bot.run(TOKEN)
