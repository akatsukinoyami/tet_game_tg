from pyrogram 		import Client, idle, ContinuePropagation
from classes.lib 	import turn_on
import traceback

class app(Client):
	config_id	= -1001328058005
	katsu_id	= 600432868
	id 				= 1661588818
	username 	= 'teto_randombot'

	switch = True

	def run_custom(self):
		self.start()

		self.bot = turn_on(self)
		self.username = self.bot.username

		idle()
		
		self.stop()

	@staticmethod
	def decorator(func):
		def wrapper(app, msg):
			if app.switch:
				try:			
						func(app, msg)
				except Exception as error:
					app.send_error(error, traceback.format_exc(), msg)
		return wrapper
			
	@staticmethod
	def id_formatter(msg):
		txt = f'**Bot:** __@teto_randbot__'
		txt+= f'\n**Chat:** __{msg.chat.title}__'
		txt+= f'\n**Chat ID:** __{msg.chat.id}__**/**__{msg.message_id}__'
		user= msg.from_user
		txt+= f'\n**User:** __{user.first_name} __'
		txt+= f'__{user.last_name}__'			if user.last_name is not None else ''
		txt+= f'__ (@{user.username})__'	if user.username  is not None else '' 
		txt+= f'\n**User ID:** __{user.id}__'
		if msg.text is not None:
			txt+= f'\n**Text:** __{msg.text.html}__'
		if msg.media is not None and msg.media:
			if msg.audio is not None:
				txt+= f'\n**Audio ID**: __{msg.audio.file_id}__'
			elif msg.document is not None:
				txt+= f'\n**Document ID**: __{msg.document.file_id}__'
			elif msg.photo is not None:
				txt+= f'\n**Photo ID**: __{msg.photo.file_id}__'
			elif msg.sticker is not None:
				txt+= f'\n**Sticker ID**: __{msg.sticker.file_id}__'
			elif msg.animation is not None:
				txt+= f'\n**Animation ID**: __{msg.animation.file_id}__'
			elif msg.video is not None:
				txt+= f'\n**Video ID**: __{msg.video.file_id}__'
			elif msg.voice is not None:
				txt+= f'\n**Voice ID**: __{msg.voice.file_id}__'
			elif msg.video_note is not None:
				txt+= f'\n**Video note ID**: __{msg.video_note.file_id}__'
			if msg.caption is not None:
				txt+= f'\n**Caption**: __{msg.caption}__'

		return txt

	def send_error(self, error, traceback, msg=None):
		if msg is not None:
			txt = '**Error occured in message:**\n\n'
			txt+= self.id_formatter(msg)
		err = f'\n**Error:** ```{str(error)}```'
		err+= f'\n**Traceback:** ```{str(traceback)}```'

		self.send_message(app.config_id, txt+err)
		self.forward_messages(app.config_id, msg.chat.id, (msg.message_id,))
		
	def send_msg(self, msg, txt):
		msg.reply(txt)

		try:
			msg.delete()
		except:
			pass
		
	@staticmethod
	def name(user):
		if user.username is not None:
			return f"**@{user.username}**" 
		elif user.last_name is not None:
			return f"**{user.first_name} {user.last.name}**"
		else:
			return f"**{user.first_name}**"