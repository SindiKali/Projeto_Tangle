import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os

# Carrega as variáveis do ambiente
load_dotenv('tangle.env')

# Configura os intents
intents = discord.Intents.default()
intents.message_content = True  # Habilita o acesso ao conteúdo das mensagens

# Cria o bot com prefixo e intents
bot = commands.Bot(command_prefix="!", intents=intents)


# Evento que avisa quando o bot tá online
@bot.event
async def on_ready():
    print(f'Bot está online!')

    # Define a atividade com imagem e texto
    activity = discord.Activity(
        type=discord.ActivityType.playing,  # Tipo: Jogando
        name="Left 4 Dead",  # Nome do jogo
        assets={
            "large_image":
            "left4dead",  # Nome exato da imagem no Developer Portal
            "large_text": "Left 4 Dead"  # Texto ao passar o mouse
        })

    # Atualiza a presença do bot
    await bot.change_presence(activity=activity)

    # Sincroniza os comandos de barra globalmente
    try:
        await bot.tree.sync()
        print(f":wrench: Comandos de barra sincronizados globalmente!")
    except Exception as e:
        print(f"Erro ao sincronizar: {e}")


# Evento que responde a mensagem "bom dia"
@bot.event
async def on_message(message):
    # Evita que o bot responda a si mesmo
    if message.author == bot.user:
        return

    # Verifica mensagens de saudação (ignorando maiúsculas/minúsculas)
    msg_lower = message.content.lower()

    if "bom dia" in msg_lower:
        await message.channel.send(f"Bom dia, {message.author.display_name}!")
    elif "boa tarde" in msg_lower:
        await message.channel.send(f"Boa tarde, {message.author.display_name}!"
                                   )
    elif "boa noite" in msg_lower:
        await message.channel.send(
            f"Boa noite, {message.author.display_name}! Tenha ótimos sonhos!")

    # Processa os comandos com prefixo (importante para que os comandos com prefixo funcionem)
    await bot.process_commands(message)


# Comando de barra: /servidor
@bot.tree.command(name="servidor", description="Endereço do servidor!")
async def servidor(interaction: discord.Interaction):
    await interaction.response.send_message('[Endereço do servidor aqui]')


# Comando de barra: /devbadge
@bot.tree.command(name="devbadge",
                  description="Link para o programa Discord Active Developer")
async def devbadge(interaction: discord.Interaction):
    await interaction.response.send_message(
        'https://discord.com/developers/active-developer')


# Inicia o bot com o token
token = os.getenv('TOKEN')
print(f'Token carregado: {token}')  # Verifica se o token está sendo carregado
bot.run(token)
