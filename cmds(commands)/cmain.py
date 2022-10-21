#導入模組
from random import random
import discord
from discord.ext import commands
from discord.ext.commands.cog import Cog
from discord.ext.commands.core import command
from core.classes import Cog_Extention        #從core(核心)底下的classes去導入Cog_Extention這個類別
import datetime
from zoneinfo import ZoneInfo
import json

with open('setting.json',mode= "r",encoding='utf8') as jfile:  #開啟setting.json #用read(r)讀取檔案 #用utf8去解碼(文字內容) #命名jfile
    jdata = json.load(jfile)  #變數jdata json去load jfile   #讀取檔案資料的東西儲存在jdata

class Main(Cog_Extention):
    #注意縮排 必須在這個類別底下 #移至類別底下後有一些功能前須加self
        #ping
    @commands.command()                                     #從command裡面調用
    async def ping(self, ctx):                               #ping代表用ping來觸發指令  #ctx表示用上下文回傳
        await ctx.send(f"{round(self.bot.latency*1000)}(ms)")    #round用來小數點後4捨5入

    @commands.command()
    async def hi(self, ctx):
       await ctx.send("小婊子不要吵!")

    @commands.command()
    async def clhs(self, ctx):
       await ctx.send("https://www.clhs.tyc.edu.tw/home")
    
    #https://cog-creators.github.io/discord-embed-sandbox/     embed生成器  #datetime出現問題
    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="SIB-Bot", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="Code By Suika", color=0xfb00ff,
        timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url="https://picrew.me/shareImg/org/202205/1453974_QItUH56T.png")
        embed.add_field(name="=em", value="Call this page.", inline=True)
        embed.add_field(name="=ping", value="Show yourr ping.", inline=True)
        embed.add_field(name="=hi", value="Maybe give you a hug.", inline=True)
        embed.add_field(name="=say", value="Make bot say something.", inline=True)
        embed.add_field(name="=gif", value="Give you a random gif.", inline=True)
        embed.add_field(name="=picture", value="Give you a picture.", inline=True)
        embed.add_field(name="=rp", value="Give you a random picture.", inline=True)
        embed.add_field(name="=urp", value="Give you a url picture.", inline=True)
        embed.set_footer(text="Still under development.")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def 幹部(self, ctx):
        embed=discord.Embed(title="幹部", color=0xf50a0a)
        embed.add_field(name="[班長]", value="馮立勝-23", inline=True)
        embed.add_field(name="[副班長]", value="阮淇祐-14", inline=True)
        embed.add_field(name="[風紀股長]", value="魯邑弘-35", inline=True)
        embed.add_field(name="[副風紀]", value="張加德-18", inline=True)
        embed.add_field(name="[學藝股長]", value="林瑀柔-02", inline=True)
        embed.add_field(name="[圖書股長]", value="鄭翔耘-34", inline=True)
        embed.add_field(name="[事務股長]", value="王禹淏-08", inline=True)
        embed.add_field(name="[副事務股長]", value="黃佳慧-07", inline=True)
        embed.add_field(name="[衛生股長]", value="李昀-01", inline=True)
        embed.add_field(name="[副衛生股長]", value="郭宥威-37", inline=True)
        embed.add_field(name="[體育股長]", value="陳約翰-21", inline=True)
        embed.add_field(name="[副體育股長]", value="鄭秉鈞-33", inline=True)
        embed.add_field(name="[資訊股長]", value="蘇昱丰-36", inline=True)
        embed.add_field(name="[環保股長]", value="江承道-09", inline=True)
        embed.add_field(name="[保健股長]", value="張翊承-19", inline=True)
        embed.add_field(name="[輔導股長]", value="蔡任冠-29", inline=True)
        embed.add_field(name="[班代]", value="孫樹宇-16", inline=True)
        embed.add_field(name="[鎖門長]", value="陳梓傑-22", inline=True)
        embed.set_footer(text="{207} 2020/08/30 [幹部]")
        await ctx.send(embed=embed)


    #機器人復誦
    @commands.command()
    async def say(self, ctx, *,msg):   #  *,msg 把所有內容都傳入
        await ctx.message.delete()
        await ctx.send(msg)           #記得給機器人管理權限!!!!!!!!

    #清理訊息
    @commands.command()
    @commands.has_permissions(administrator = True)  #需有管理權限才可觸發指令
    async def clean(self, ctx, num:int):       #註解num為整數int資料型態 可不必再轉換資料型態
        await ctx.channel.purge(limit = num+1)   #limit上限值 #數量為num #也要把指令那則刪掉(+1) 
 

async def setup(bot):                                             #初始化設定bot
   await bot.add_cog(Main(bot))                                 #新增這個cog 傳入bot.py裡面的bot