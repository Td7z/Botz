from google.cloud import texttospeech_v1beta1 as texttospeech
from twitchio.ext import commands

# Restante do código...

# Substitua pelas suas credenciais
client_id = "gp762nuuoqcoxypju8c569th9wz7q5"
client_secret = "ypco6er9g17yzbngrlxpvgfr6g7csp"
oauth_token = "oauth:sum22gpyyij84mvo5d33zh84jhvwy2"
channel_name = "zerinonze"

# Conecta ao chat da Twitch
bot = commands.Bot(
    token=oauth_token,
    client_id=client_id,
    nick="hawkinngx",
    prefix="!",  # Corrigido para string
    initial_channels=[channel_name],
)

@bot.command(name="gpt")
async def generate_question(ctx):
    # Gera uma pergunta usando a API Generative AI
    client = texttospeech.CompletionClient()
    completion = client.generate_completion(
        request={"prompt": "Crie uma pergunta interessante para o chat da Twitch:", "max_tokens": 32, "temperature": 0.7}
    )
    question = completion.text.strip()

    # Envia a pergunta para o chat
    await ctx.send(f"{question}")

if __name__ == "__main__":
    bot.run()