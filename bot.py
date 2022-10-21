#導入模組
from tkinter.tix import MAIN
from wsgiref.util import request_uri
import discord
from discord import channel
from discord.activity import Game
from discord.ext import commands
from discord.flags import Intents
import json                               #設定檔模組
import random                             #導入random
import os
import asyncio


with open('setting.json',mode= "r",encoding='utf8') as jfile:  #開啟setting.json #用read(r)讀取檔案 #用utf8去解碼(文字內容) #命名jfile
    jdata = json.load(jfile)  #變數jdata json去load jfile   #讀取檔案資料的東西儲存在jdata

#建置Bot實體
bot = commands.Bot(command_prefix = '=' , intents = discord.Intents.all())   #(command_prefix)為呼叫機器人的字首 #訂閱特定事件

#調用event函式庫
@bot.event
async def on_ready():       #觸發on_ready的事件
    #這邊設定機器人的狀態
    #discord.Status.<狀態>，可以是online（上線）,offline（下線）,idle（閒置）,dnd（請勿打擾）,invisible（隱身）
    status_w = discord.Status.idle
    
    #這邊設定機器當前的狀態文字
    #type可以是playing（遊玩中）、streaming（直撥中）、listening（聆聽中）、watching（觀看中）、custom（自定義）
    activity_w = discord.Activity(type=discord.ActivityType.watching, name="西瓜一族")
    await bot.change_presence(status= status_w, activity=activity_w)
    print(">>Bot睡飽了!<<")     #寫在終端機

#成員加入已移至event


#成員離開已移至event

#ping已移至main

#picture已移至react

#load指令
@bot.command() #調用commands庫                                          
async def load(ctx, extension):                      #定義load 傳入extention的名稱
    bot.load_extension(f'cmds(commands).{extension}')    #呼叫load_extention 
    await ctx.send (f'讀取{extension}')             #跑完指令後回傳

#unload
@bot.command() #調用commands庫                                          
async def unload(ctx, extension):                      #定義unload 傳入extention的名稱
    bot.unload_extension(f'cmds(commands).{extension}')    #呼叫unload_extention 
    await ctx.send (f'取消讀取{extension}')             #跑完指令後回傳

#reload
@bot.command() #調用commands庫                                          
async def reload(ctx, extension):                      #定義reload 傳入extention的名稱
    bot.reload_extension(f'cmds(commands).{extension}')    #呼叫reload_extention 
    await ctx.send (f'重新讀取{extension}')             #跑完指令後回傳


async def load_extensions():
    for filename in os.listdir('D:\Suika\git hub desktop\SIB-Bot\cmds(commands)'):      #for迴圈 語法for變數名稱in 呼叫os模組底下的listdir(可以列出底下的資料夾有哪些)從cmds裡
        if filename.endswith('.py'):           #if判斷只讀取名稱結尾是.py的文件
            await bot.load_extension(f'cmds(commands).{filename[:-3]}') #bot去讀取cmds底下的filename [:-3]省略掉最後3個字


async def main():
    async with bot:
        await load_extensions()
        await bot.start(jdata['token'])
        
asyncio.run(main())
