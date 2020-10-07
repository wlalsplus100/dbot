import discord
import asyncio
import random
import datetime
import time
import urllib
import bs4

now = datetime.datetime.now()

client = discord.Client()

token = "NzQ3NjA1MTExODE1MDEyMzky.X0RThA.G49jSIUg_cf6OUUKZVc6oFXFWbc"

a = 0

partyone = []


English_word = ['발생하다','-이다,있다','-이 되다','시작하다','물다','부서지다,깨다','가져오다','짓다,건축하다','사다,구입하다','잡다','오다','자르다,베다','파다','하다','먹다','떨어지다','느끼다','싸우다,다투다','찾다,발견하다','설립하다,세우다']

hit = 0





@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("===================")
    game = discord.Game("다람봇 작동")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    
    
    if message.author == client.user:
        return

    if message.author.bot:
        return

    if message.content.startswith("ㅎㅇ"):
        await message.channel.send("님도 ㅎㅇ")

    if message.content == ('야'):
        await message.channel.send('왜')

    if message.content.startswith('ㄹㅇ ㅋㅋ'):
        await message.channel.send('fd zz')

    if message.content.startswith('ㄹㅇㅋㅋ'):
        await message.channel.send('fdzz')

    if message.content.startswith('!명령어'):
        await message.channel.send(embed=discord.Embed(description='!명령어[명령어를 알려준다]\n \
        !주사위[주사위를 굴려 결과를 알려준다]\n \
        !따라하기 a[a라고 말한다.만약 이상한것을 말하게 할 시 다람봇이 그 사람을 무시할 예정]\n \
        !시간[현재 시간을 알려준다]\n!이근 대위 어록[이근 대위의 어록을 보여준다]\n \
        !타이머 int[설정한 int만큼 초를 세고 초를 다 세면 알려준다.int 너무 길게 하면 혼난다]\n \
        !암호[너희들이 적어도 이번 년도 동안은 절대 못풀 것같은 암호를 보여준다]\n \
        !정답 암호정답[암호 정답을 맞춘다면 특정 메세지가 나온다.]\n\
        !모집 (파티 관련 내용)[파티를 모집한다.파티 관련 내용을 적으면 추가로 적어준다.\n참가 인원이 5명이 되면 알려줌]\n\
        !참가[모집중인 파티에 참가 한다]\n\
        !파티 현황[파티에 참가한 인원,파티에 참가한 사람의 이름을 알려준다]\n\
        !파티 초기화[무분별한 사용을 막기위해 관리자만 사용할 수 있게 막은 명령어,파티를 초기화 한다.]'))

    if message.content.startswith('!주사위'):
            randomNum = random.randrange(1,7)
            print(randomNum)
            if randomNum == 1:
                await message.channel.send(message.channel, embed=discord.Embed(description='주사위의 숫자는: ' + ':one:'))
            if randomNum == 2:
                await message.channel.send(message.channel, embed=discord.Embed(description='주사위의 숫자는: ' + ':two:'))
            if randomNum == 3:
                await message.channel.send(message.channel, embed=discord.Embed(description='주사위의 숫자는: ' + ':three:'))
            if randomNum == 4:
                await message.channel.send(message.channel, embed=discord.Embed(description='주사위의 숫자는: ' + ':four:'))
            if randomNum == 5:
                await message.channel.send(message.channel, embed=discord.Embed(description='주사위의 숫자는: ' + ':five:'))
            if randomNum == 6:
                await message.channel.send(message.channel, embed=discord.Embed(description='주사위의 숫자는: ' + ':six:'))

    if message.content.startswith("!따라하기"):
        message_replaced = message.content.replace("!따라하기", "")
        await message.channel.send(message_replaced)

    if message.content == ('!시간'):
        await message.channel.send(now)

    if message.content.startswith('다람봇 바보'):
        await message.channel.send('하하\nㅗ(^.^)ㅗ')

    if message.content.startswith('온라인 수업') or message.content.startswith('온라인수업'):
        await message.channel.send('난 안함 ㅋㅋㄹㅃㅃ')

    if message.content == ('닥쳐'):
        await message.channel.send('싫은데?')

    if message.content.startswith('지건마렵네?') or message.content.startswith('지건 마렵네?'):
        await message.channel.send('때려보셈 ㅋㅋㄹㅃㅃ')

    if message.content == ('sake L'):
        await message.channel.send('sake L:네\n기자:당신은 미래를 볼 수 있나요?')

    if message.content.startswith('심심해'):
        await message.channel.send('그래서 나보고 어쩌라고')

    if message.content == ('다람봇 끝말잇기'):
        await message.channel.send('나 크시 아니다')

    if message.content == ('롤'):
        await message.channel.send('확실한건 히오스보다는 갓겜이다.')

    if message.content.startswith('ㅇㅈ'):
        await message.channel.send('ㅇ ㅇㅈ')

    if message.content.startswith('!ㅔ'):
        await message.channel.send('!p 임 ㅋㅋㅋㅋ')

    if message.content.startswith('다람봇'):
        await message.channel.send('?')

    if message.content.startswith('과제 알려줘'):
        await message.channel.send('니가 직접봐 ^^ㅣ')

    if message.content == ('!이근 대위 어록'):
        await message.channel.send('너 인성문제 있어?\n머리부터 발끝까지\n \
우리 할머니가 그것보단 빨리 뛰겠다\n\
너 숨쉬지마 너 양치안했지\n니 엉덩이 자랑하고 싶냐?\n\
너가 AV배우야?소리내지마')

    if message.content.startswith('이번주 롤 토요일 10시'):
        await message.channel.send('늦으면 버리고 한다')

    if message.content.startswith('심심해'):
        time.sleep(1)
        await message.channel.send('크시랑 끝말잇기나 해 ㅋ')

    if message.content.startswith('!타이머'):
        message_replaced = message.content.replace("!타이머", "")
        timeout = int(message_replaced)
        if timeout <= 180:
            await asyncio.sleep(timeout)
            await message.channel.send('타이머 종료!')
            await asyncio.sleep(0.5)
            await message.channel.send('타이머 종료!')
            await asyncio.sleep(0.5)
            await message.channel.send('타이머 종료!')
        else:
            await message.channel.send('타이머 기능은 180초 이상부터는 봇의 원활한 이용을 위해 금지함')

    if message.content == ('!암호'):
        await message.channel.send('16,01,89,8')
        await message.channel.send('내 생각에 너희들은 절대 못풀 암호 같아')

    if message.content.startswith('!정답'):
        if message.content.endswith('shaco') or message.content.endswith('Shoco') or message.content.endswith('샤코'):
            await message.channel.send('드디어 이 문제를 맞췄군...')
            await message.channel.send('그래서 지금이 몇년도?')
        else:
            await message.channel.send('땡!')
            await message.channel.send('니가 못 맞출줄 알았지')

    if message.content.startswith('정답이 뭔데'):
        await message.channel.send('안 알랴줌')

    if message.content.startswith('등교날'):
        await message.channel.send('2020-09-23')

    if message.content.startswith('!tts'):
        msg = message.content
        msg = msg.split(" ")[1]
        sender = message.author
        str(sender)
        await message.channel.send(sender)
        await message.channel.send('님이 tts 메세지를 요청하였습니다.')
        await message.channel.send(msg,tts=True)

    if message.content.startswith('둠상필'):
        await message.channel.send('둠너필')
        await message.channel.send('둠너필')
        await message.channel.send('둠너필')
        await message.channel.send('둠너필')
        await message.channel.send('둠너필')

    if message.content == ('야필패'):
        await message.channel.send('이게 마따')

    if message.content == ('!시간표'):
        await message.channel.send("월요일:영어회화,기술가정,음악,도덕,국어,스포츠\n \
화요일:수학,예체1,기술가정,영어,과학,예체2,창체\n \
수요일:사회,수학,체육,도덕,과학,기술가정,예체1\n \
목요일:기술가정,수학,진로,진로,국어,선택,선택\n \
금요일:사회,국어,선택,선택,미술,영어,창체")

    if message.content == ('ㅈㄱㅊㅇ'):
        await message.channel.send('꼬우면 너도 ㅈㄱ하셈ㅋㅋ')

    if message.content.startswith('!모집'):
        global a
        global partyone
        word = message.content.split('!모집')[1]
        a = a + 1
        sender = str(message.author)
        await message.channel.send(sender + '(이)가 파티를 모집합니다!\n\
파티에 참여 하려면 !참가를 써주세요.\n현재 파티 참가 인원:' + ':one:')
        
        await message.channel.send('파티 관련 내용:' + word)
        partyone.append(message.author)

    if message.content == ('!참가'):
        if a >= 1:
            a = a + 1
            partyone.append(message.author)
            sender = str(message.author)
            if a == 2:
                await message.channel.send(sender + '(이)가 파티에 참가 했습니다!\n파티 참가 인원:' + ':two:')
        
            elif a == 3:
                await message.channel.send(sender + '(이)가 파티에 참가 했습니다!\n파티 참가 인원:' + ':three:')
        
            elif a == 4:
                await message.channel.send(sender + '(이)가 파티에 참가 했습니다!\n파티 참가 인원:' + ':four:')

            elif a == 5:
                await message.channel.send(sender + '(이)가 파티에 참가 했습니다!\n파티 참가 인원:' + ':five:' + '\n파티 완성\n파티원 목록:')
                for b in partyone:
                    await message.channel.send(b)

    if message.content == ('!파티 현황'):
        if a == 1:
            await message.channel.send('파티 참가 인원' + ':one:')
            for b in partyone:
                await message.channel.send(b)
        if a == 2:
            await message.channel.send('파티 참가 인원' + ':two:')
            for b in partyone:
                await message.channel.send(b)
        if a == 3:
            await message.channel.send('파티 참가 인원' + ':three:')
            for b in partyone:
                await message.channel.send(b)
        if a == 4:
            await message.channel.send('파티 참가 인원' + ':four:')
            for b in partyone:
                await message.channel.send(b)
        if a == 5:
            await message.channel.send('파티 참가 인원' + ':five:')
            for b in partyone:
                await message.channel.send(b)

    if message.content == ('!파티 초기화'):
        sender = str(message.author)
        if sender == ('다람쥐도쥐라구찍#8315'):
            a = 0
            partyone = []
            await message.channel.send('파티를 초기화 했습니다')


                            
        


        
            

                                       

client.run("NzQ3NjA1MTExODE1MDEyMzky.X0RThA.G49jSIUg_cf6OUUKZVc6oFXFWbc")
    

