import discord, datetime, typing
from discord.ext import commands
from itertools import product

@client.command()
@commands.has_permissions(manage_channels = True)
async def slowmode(ctx, channel: typing.Optional[discord.TextChannel], amount: typing.Optional[int]):
    if amount == None:
        amount = 1

    if amount > 21600:
        embed = discord.Embed(title=f"", description=":x: Slowmode Komutu İçin Maksimum Sayı `21600`.", color=discord.Colour.red())
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed, delete_after=5)
        return

    if amount < 0:
        embed = discord.Embed(title=f"", description=":x: Sayı Pozitif Yönde Olmalıdır.", color=discord.Colour.red())
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed, delete_after=5)
        return

    if channel == None:
        channel = ctx.channel

    hhmmss = []
    for (h, m, s) in product(range(24), range(60), range(60)):
        hhmmss.append("%02d Saat, %02d Dakika, %02d Saniye" % (h, m, s))

    try:
        await channel.edit(slowmode_delay=amount)
        if amount == 0:
            embed = discord.Embed(title=f"", description=f":white_check_mark: <#{str(channel.id)}> Kanalında Slowmode Artık **Kapatıldı**!", color=discord.Colour.teal())
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"", description=f":white_check_mark: <#{str(channel.id)}> Kanalında Slowmode Artık `{hhmmss[amount]}` Olarak Ayarlandı!", color=discord.Colour.teal())
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
    except Exception:
        embed = discord.Embed(title=f"", description=f":x: Kanalda Yavaşlama Modunu Ayarlamak İçin Gereken Yetkiye Sahip Değilim.", color=discord.Colour.red())
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed, delete_after=5)