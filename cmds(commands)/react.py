#導入模組
import imp
import discord
from discord.ext import commands
from core.classes import Cog_Extention
import random
import json
import datetime

with open('setting.json',mode= "r",encoding='utf8') as jfile:  #開啟setting.json #用read(r)讀取檔案 #用utf8去解碼(文字內容) #命名jfile
    jdata = json.load(jfile)  #變數jdata json去load jfile   #讀取檔案資料的東西儲存在jdata


class React(Cog_Extention):
    #注意縮排 功能需在類別底下  #移至類別底下後有一些功能前須加self
    #picture
    @commands.command()                                     #從command裡面調用
    async def picture(self , ctx):                            #設定picture來觸發
      pic = discord.File(jdata['picture'])           #變數pic設定為discord內建的file來傳送和讀取
      await ctx.send(file = pic)                     #以讀取檔案的方式來傳送

    @commands.command()
    async def 課表(self , ctx):
      classpage = discord.File(jdata['課表'])
      await ctx.send(file = classpage)

    @commands.command()                                     #從command裡面調用
    async def rp(self , ctx):                                 #設定rp來觸發
      rp = random.choice(jdata['r_picture'])         #讀取r_picture 再隨機挑選
      rp = discord.File(rp)                          #以discord內建的file來傳送和讀取
      await ctx.send(file = rp)                      #以讀取檔案的方式來傳送

    @commands.command()                                     #從command裡面調用
    async def urp(self , ctx):                                #設定urp來觸發
      urp = random.choice(jdata['url_picture'])      #讀取urp_picture 再隨機挑選
      await ctx.send(urp)                            #以讀取!!文字!!的方式來傳送
    
    @commands.command()
    async def gif(self, ctx):
      gif = random.choice(jdata['GIF'])
      gif = discord.File(gif)
      await ctx.send(file = gif)

    @commands.command()
    async def nowtime(self, ctx):
      now = datetime.datetime.now()
      await ctx.send(now)

async def setup(bot):                                             #初始化設定bot
    await bot.add_cog(React(bot))                                 #新增這個cog 傳入bot.py裡面的bot
