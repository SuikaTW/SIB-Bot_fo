from asyncio.tasks import sleep, wait
from encodings import utf_8
from ssl import SSLEOFError
from time import time
import discord
from discord.ext import commands
from core.classes import Cog_Extention
import json,asyncio,datetime
import datetime

class task(Cog_Extention):                                  
    def __init__(self,*args, **kwargs):          #初始化設定 *args **kwargs 將不定量的參數傳給函式 (__init__)為class初始化設定
        super().__init__(*args, **kwargs)        #第二次初始化設定(__init__)
        self.counter = 0

        async def interval():
            await self.bot.wait_until_ready()      #等到bot啟動完
            self.channel = self.bot.get_channel(916608296838905856)  #bot 得到要傳送頻道的id
            while not self.bot.is_closed():         #如果機器人未關閉(也就是機器人在線上)
               nowtime = datetime.datetime.now().strftime('%Y %m %d %H %M %S')
               await self.channel.send("Bot online")    #傳送到channel
               await self.channel.send(f"現在時間:{nowtime}")
               await asyncio.sleep(86400) #asyncio底下的功能 #單位:秒
    
        self.bg_task = self.bot.loop.create_task(interval()) #創建一個背景作業的task 取名叫bg_task #bot重複執行
        
    @commands.command()
    async def set_channel(self, ctx,ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel: {self.channel.mention}')

    @commands.command()
    async def set_time(self, ctx, time ):
        with open('setting.json','r',encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata['time'] = time
        with open('setting.json','w',encoding='utf8') as jfile:
            json.dump(jdata,jfile, indent = 4)
            

        async def time_task():
            await self.bot.wait_until_ready()      #等到bot啟動完
            self.channel = self.bot.get_channel(916608296838905856)  #bot 得到要傳送頻道的id
            while not self.bot.is_closed():         #如果機器人未關閉(也就是機器人在線上)
               nowtime = datetime.datetime.now().strftime('%w %H %M')
               with open('setting.json','r',encoding='utf8') as jfile:
                jdata = json.load(jfile)
                if nowtime == jdata['time'] and self.counter == 0:
                    await self.channel.send('test')
                    self.counter = 1
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    self.counter = 0
                    pass

        self.time_task = self.bot.loop.create_task(time_task())
            
        
async def setup(bot):                                             #初始化設定bot
    await bot.add_cog(task(bot))