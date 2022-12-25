#requirements
#py-cord==2.3.0

import discord, string
import random as keygen

with open("inactivekeys.txt", "r") as f:
    inactivekeys = f.read()
with open("usedkeys.txt", "r") as f:
    usedkeys = f.read()

client = discord.Bot()

@client.slash_command(description="Generates a license key!")
async def generatekey(ctx):

    if ctx.author.id == 1007561535952011285:
        pass
    else:
        return

    key = ''.join(keygen.choices(string.ascii_letters, k=16))
    with open("inactivekeys.txt", "a") as f:
        f.write(f"{key}\n")

    await ctx.respond(f":newspaper: Inactive license key created:\n`{key}`")

@client.slash_command(description="Redeem a license key!")
async def redeem(ctx, key):

    if len(key) != 16:
        print("Key_1 error")
        em = discord.Embed(description=f"You don't have any assigned keys!", color=0xA601F9)
        await ctx.respond(embed=em)
        return
        

    if key not in inactivekeys and key not in usedkeys:
        print("Key_2 error")
        em = discord.Embed(description=f"You don't have any assigned keys!", color=0xA601F9)
        await ctx.respond(embed=em)
        return


    if key in usedkeys and key not in inactivekeys:
        print("Key_3 error")
        em = discord.Embed(description=f"You don't have any assigned keys!", color=0xA601F9)
        await ctx.respond(embed=em)
        return

    if key not in usedkeys and key in inactivekeys:

        with open("ids.txt", "r") as f:
            ids = f.read()

            if str(ctx.author.id) in ids:
                em = discord.Embed(description=f"You are already whitelisted!", color=0xA601F9)
                await ctx.respond(embed=em, ephemeral=True)
                return
            else:
                with open("ids.txt", "a") as f:
                    f.write(f"{ctx.author.id} | {ctx.author}\n")

                    role = discord.utils.get(ctx.guild.roles, name="Customers")
                    await ctx.author.add_roles(role)

                    em = discord.Embed(description=f"Succesfully redeemed the key!", color=0xA601F9)
                    await ctx.respond(embed=em)
                    
client.run("")
