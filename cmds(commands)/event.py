#導入模組
import imp
from random import random
import discord
from discord import message
from discord.ext import commands
from discord.ext.commands.cog import Cog
from discord.ext.commands.core import command
from core.classes import Cog_Extention        #從core(核心)底下的classes去導入Cog_Extention這個類別
import json
import random


with open('setting.json',mode= "r",encoding='utf8') as jfile:  #開啟setting.json #用read(r)讀取檔案 #用utf8去解碼(文字內容) #命名jfile
    jdata = json.load(jfile)  #變數jdata json去load jfile   #讀取檔案資料的東西儲存在jdata

class event(Cog_Extention):                 #繼承cog_extention
    #成員加入
    @commands.Cog.listener()                           #commands底下的cog底下的listener(傾聽者 偵測事件跟event相似)  
    async def on_member_join(self, member):                 #觸發on_member_join的事件
     channel = self.bot.get_channel(int(jdata['member_join']))   #channel的變數 #jdata回傳的資料是字串型態 須強制轉換成數字
     await channel.send(f"{member} 進來ㄌ!") 

    #成員離開
    @commands.Cog.listener()                           #commands底下的cog底下的listener(傾聽者 偵測事件跟event相似)  
    async def on_member_remove(self, member):                 #觸發on_member_remove的事件
     channel = self.bot.get_channel(int(jdata['member_leave']))  #channel的變數 #jdata回傳的資料是字串型態 須強制轉換成數字
     await channel.send(f"{member} 離開ㄌ!")


    @commands.Cog.listener()
    async def on_message(self, msg):               #觸發on_message 當使用者在輸入訊息時  msg:使用者傳入的訊息
        benny = ['bj','BJ','奔尼眷','BennyJeng','bennyjeng','benny','Benny','Bennyjeng']
        lol = ['lol','笑死','咲死','lmao','lmfao']
        if msg.content in benny and msg.author != self.bot.user:   #判斷content內容完全等於字串and這則訊息的作者不是機器人才能觸發
            BJgif = discord.File(jdata['BJgif'])
            await msg.channel.send("BennyJeng... BENNYJENG IS REAL!!!")  
            await msg.channel.send(file = BJgif)              #上面符合後觸發傳送訊息
        elif msg.content in lol and msg.author != self.bot.user:  
            feedback = random.choice(jdata['lolfeedback'])
            await msg.channel.send(feedback)      

async def setup(bot):                                             #初始化設定bot
    await bot.add_cog(event(bot))                                 #新增這個cog 傳入bot.py裡面的bot