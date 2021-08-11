import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("느트르봇 준비 완료!!")
    game = discord.Game("오리 여친이랑")
    await client.change_presence(status=discord.Status.online, activity=game)




@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('가오리이이'):
        await message.channel.send('네 다음 느타리 ㅋㅋㅋ')
    if message.content.startswith('랙티아'):
        await message.channel.send('랙ㅋㅋㅋ티ㅋㅋㅋㅋ아ㅋㅋㅋㅋ')
    if message.content.startswith('킥킥'):
        await message.channel.send('벤 ㄱㄱ')
    if message.content.startswith('느트르봇'):
        await message.channel.send('ㅎㅇ')
    if message.content.startswith('ㅎㅇ'):
        await message.channel.send('ㅇㅇ')
    if message.content.startswith('ㄹㅇㅋㅋ'):
        await message.channel.send('ㄹㅇㅋㅋ')
    if message.content.startswith('니엄마'):
        await message.channel.send('조예성')
    if message.content.startswith('와루'):
        await message.channel.send('너도 ㄴㅌㄹ 당할래?')
    if message.content.startswith('우달'):
        await message.channel.send('왜')
    if message.content.startswith('심심해'):
        await message.channel.send('친구 없어서?')
    if message.content.startswith('렉티아'):
        await message.channel.send('렉ㅋㅋㅋ티ㅋㅋㅋㅋ아ㅋㅋㅋㅋ')
    if message.content.startswith('ㄴㅌㄹ'):
        await message.channel.send('가오리이이 ㅠㅜㅠㅜ')
    if message.content.startswith('개미왕자'):
        await message.channel.send('발지훈!!!!')
    if message.content.startswith('예아'):
        await message.channel.send('예아가 왜 일베임ㅋㅋ')
    if message.content.startswith('삼치'):
        await message.channel.send('는 사치')
    if message.content.startswith('아상이'):
        await message.channel.send('아가리')
    if message.content.startswith('ㅋㅋㅋㅋㅋ'):
        await message.channel.send('웃어?')
    if message.content.startswith('ㄵ'):
        await message.channel.send('누텔라잼~')
    if message.content.startswith('ㄴㅈ'):
        await message.channel.send('누텔라잼~')
    if message.content.startswith('!ㅗ'):
        await message.channel.send('ㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗ')
    if message.content.startswith('리바이브'):
        await message.channel.send('ntr')
    if message.content.startswith('푸고'):
        await message.channel.send('언제옴?')
    if message.content.startswith('ㅈㅅ'):
        await message.channel.send('알면 됐음')
    if message.content.startswith('1118'):
        await message.channel.send('커가 코요')
    if message.content.startswith('코가'):
        await message.channel.send('커요')
    if message.content.startswith('발이'):
        await message.channel.send('커요')
    if message.content.startswith('배댐그랩'):
        await message.channel.send('배댐그랩 이지랄 ㄴㄴ')
    if message.content.startswith('ㅋㅂ'):
        await message.channel.send('ㄴㅈ')
    if message.content.startswith('ㄴㄴ'):
        await message.channel.send('뭐가 ㄴㄴ임 ㅋㅋㅋㅋ')
    if message.content.startswith('십자가'):
        await message.channel.send('야')
        await message.channel.send('개토래이 몰라?')
        await message.channel.send('너 조선족이지')
        await message.channel.send('나한테 기생해서 100k 이상 가는거 봤어 ㅋㅋ')
        await message.channel.send('네 다음 핵쟁이~')
    if message.content.startswith('ㅅㅂ'):
        await message.channel.send('ㅅㅂ')
    if message.content.startswith('뭉탱이'):
        await message.channel.send('뭉탱이로 발링게슝')
    if message.content.startswith("'해줘'"):
        await message.channel.send('지랄좀 ㅋㅋ')
    if message.content.startswith("ㅠ"):
        await message.channel.send('울면 응딩이에 털남 슥어~')
    if message.content.startswith("ㅜ"):
        await message.channel.send('울면 응딩이에 털남 슥어~')
    if message.content.startswith('ㅗ'):
        await message.channel.send('ㅗ')
    if message.content.startswith('발가락'):
        await message.channel.send('존맛탱')
    if message.content.startswith('ㅇㅈㄹ'):
        await message.channel.send('ㄹㅇㅋㅋ')
    if message.content.startswith('ㅇㅅㅇ'):
        await message.channel.send('ㅎㅅㅎ')
    if message.content.startswith('ㅇㅋㅌ'):
        await message.channel.send('ㅈㅋㅌ!!')
    if message.content.startswith('ㅁ '):
        await message.channel.send('마이펫하냐? ㅋㅋ')
    if message.content.startswith('ㅃㄹ'):
        await message.channel.send('서둘러~')
    if message.content.startswith('ㅇㅈ?'):
        await message.channel.send('ㅇㅈ!')
    if message.content.startswith('포기'):
        await message.channel.send('는 배추 세는 단위')
    if message.content.startswith('닥쳐'):
        await message.channel.send('시른뒈~')
    if message.content.startswith('로어그랩!'):
        await message.channel.send('호로로롥로로로롤롤롥')
    if message.content.startswith('워터핀'):
        await message.channel.send('워터핀 모르노? ㅈ뉴비네 ㅋ')
    if message.content.startswith('모르노?'):
        await message.channel.send('ㅈ뉴비네')
    if message.content.startswith('ㅈ뉴비네'):
        await message.channel.send('ㄹㅇㅋㅋ')
    if message.content.startswith('ㅇㅂㅇ'):
        await message.channel.send('ㅇㅍㅇ')
    if message.content.startswith('ㅇㅈㅇ'):
        await message.channel.send('ㅇㅊㅇ')
    if message.content.startswith('ㅇㄷㅇ'):
        await message.channel.send('ㅇㅌㅇ')
    if message.content.startswith('ㅇㄱㅇ'):
        await message.channel.send('ㅇㅋㅇ')
    if message.content.startswith('나에스'):
        await message.channel.send('로리콘은 무죄')
    if message.content.startswith('여긴'):
        await message.channel.send('응디 시 티~')
    if message.content.startswith('ㅑ'):
        await message.channel.send('ㅙ')
    if message.content.startswith('!ㅂㅌ'):
        await message.channel.send('ㅂㅌ')
    if message.content.startswith('ㅂㅂ'):
        await message.channel.send('잘가')
    if message.content.startswith('나 랙티아임 깝ㄴㄴ'):
        await message.channel.send('랙티아 좆병신 ㅋㅋㅋㅋㅋㅋㅋ')
    if message.content.startswith('?'):
        await message.channel.send('?')
    if message.content.startswith('응디'):
        await message.channel.send('씰룩씰룩~')
    if message.content.startswith('슴름'):
        await message.channel.send('다 제가 만든거에요 ㅎㅎ')
    if message.content.startswith('SM'):
        await message.channel.send('헤응ㅇ 찰싹')
    if message.content.startswith('끼어들지'):
        await message.channel.send('ㅇㅉ')



client.run(os.environ['token'])