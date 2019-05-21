import discord


async def delete(message,clientn):
    for servers in clientn.guilds:
        if servers.name == message.guild.name:
            SERVER_OBJECT = servers
            SERVER_NAME = servers.name
            break
    print("\nScanning " + SERVER_NAME)
    for channel in SERVER_OBJECT.text_channels:
        # Cycle through channels where you have permissions (chats)
        clientpermissions = channel.guild.me.permissions_in(channel)
        read = clientpermissions.read_messages
        send = clientpermissions.send_messages
        permissionstring = False
        if read and send:
            permissionstring = True
        print("Scanning: " + channel.name + " | Permissions: " + str(permissionstring))
        if read and send:
            async for messages in channel.history(limit=int(500)):
                if messages.author == clientn.user:
                    if not messages.content:
                        print("Deleting: PICTURE")
                    else:
                        print("Deleting: " + messages.content)
                    await discord.Message.delete(messages)

