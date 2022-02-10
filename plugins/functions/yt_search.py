from pyrogram import Client ,filters
import os
from py_youtube import Data, Search 
from pyrogram.types import *




@Client.on_inline_query()
async def start(client,message):
	await message.reply_text("Helo iam Youtube Video Search\nUse in inline mode")
	


@app.on_inline_query()
async def search_video(client,query):
	search = []
	result = Search(query.query.strip()).videos()
	for i in result:
		try:
			title = i["title"]
			id = i["id"]
			data = i["simple_data"]
		except:
			pass
		try:
			search.append(
                InlineQueryResultPhoto(
                    title=title,
                    description=data,
                    caption="https://youtu.be/"+id))
		
		except:
		          pass
            
	await query.answer(search)
