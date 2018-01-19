import discord
from discord import Embed, Color

import QUERIES

description = 'New'

async def ex(message, client):
    QUERIES.create_connection(QUERIES.DB_FILE)
    
    head, sep, msg = message.content.partition(' ')
    
    data = msg.split("@")
    x = msg.count("@")
    players = message.mentions

    if x == 1:
        p2 = msg
        await client.send_message(message.channel, 'Player 2 is {}'.format(p2))
    elif x == 2:
        p2, sep, p3 = msg.partition(' ')
        await client.send_message(message.channel, 'Player 2 is {0}, Player 3 is {1}'.format(p2, p3))
    elif x == 3:
        p2, sep, p3, p4 = msg.partition(' ')
        await client.send_message(message.channel, 'Player 2 is {0}, Player 3 is {1}, Player 4 is {2}'.format(p2, p3, p4))

    userid = message.author.id
    userName = message.author

    i = 1

    while i <= x:
        if i == 1:
            gtLoc = data[i].find('>')
            player2_id = data[i][0:gtLoc]
        if i == 2:
            gtLoc = data[i].find('>')
            player3_id = data[i][0:gtLoc]
        if i == 3:
            gtLoc = data[i].find('>')
            player4_id = data[i][0:gtLoc]
    
        i += 1

    if x == 1:
        player3_id = 0
        player4_id = 0
    elif x == 2:
        player4_id = 0

    # 1. Bot gets current Game ID from DB
    gameID = QUERIES.get_current_game_id(QUERIES.DB_FILE)

    # 2. Bot creates new channel
    #       #monopoly-game-<Game ID>
    channelName = 'monopoly-game-{}'.format(gameID)
    channel = await client.create_channel(message.server, channelName, type=discord.ChannelType.text)  

    # 3. New Game ID inserted into table
    QUERIES.create_new_game_channel(QUERIES.DB_FILE, userid, player2_id, player3_id, player4_id)

    # 4. Bot creates new role
    #       monopoly-game-<Game ID>-players
    roleDef = 'Monopoloy Game {} Player'.format(gameID)

    await client.create_role(message.server, name=roleDef, hoist=True, mentionable=False)
    role = discord.utils.get(message.server.roles, name=roleDef)
    await client.add_roles(userName, role)
    for player in players:
        await client.add_roles(player, role)
    #await client.add_roles(discord.Member.mentioned_in(message.content), role)

    
    #ply2 = discord.Member.add_roles()
    #await discord.Member.add_roles(p2, role)

    #if x == 1:
        #await client.add_roles(discord.Member.mentioned_in(message), role)
    #if x == 2:
        #await client.add_roles(discord.Member.get_user(p2), role)
        #await client.add_roles(discord.Member.get_user(p3), role)
    #if x == 3:
        #await client.add_roles(p2, role)
        #await client.add_roles(p3, role)
        #await client.add_roles(p4, role)

    
    # 5. Bot promptes message.author to invite players to the game
    #await client.send_message(channel, embed=discord.Embed(
                                                            #color=discord.Color.green(),
                                                            #description=('Who is going to be player 2? Type \"p2\"'),))

    #msg = await client.wait_for_message(message.content)

    #await client.send_message(channel, msg.author + ' is player 2')



    # 6. Bot gets player ids of players and inserts them into the info about the game.

    