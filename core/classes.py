#導入模組
import discord
from discord.ext import commands
   #之後只需繼承Cog_Extention 底下定義的全部都會繼承進去
class Cog_Extention(commands.Cog):       #建立類別Cog_Extention類別 繼承commands底下的Cog
    def __init__ ( self, bot):           #初始化功能init裡面要放self 放入bot作為傳入用
        self.bot = bot                   #定義這個類別的bot就是bot.py裡面那個bot(將bot.py裡的bot傳入)