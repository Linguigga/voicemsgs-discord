@bot.command('audiotovoice')
async def audiotovoice(ctx, *, filepath_url: str = None):
	file_url = None
	filepath = None
	if not filepath_url:
		file_url = ctx.message.attachments[0].url
	if filepath_url:
		if filepath_url.startswith('https://'):
			file_url = filepath_url
		else:
			filepath = filepath_url
	if file_url:
		r = requests.get(file_url)
		file_content = r.content
	if filepath:
		with open(filepath, 'rb') as r:
			file_content = r.read()
	con_len = len(str(file_content))
	await ctx.message.delete()
	headersforthisshit = {"Content-Length":"6969","User-Agent":"Discord/42954 CFNetwork/1390 Darwin/22.0.0","Authorization":master_token,"x-debug-options":"bugReporterEnabled","Accept-Language":"en-NZ","x-discord-locale":"en-US","Accept":"*/*","Content-Type":"application/json","x-super-properties":"eyJvcyI6ImlPUyIsImJyb3dzZXIiOiJEaXNjb3JkIGlPUyIsImRldmljZSI6ImlQaG9uZTExLDIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tTloiLCJjbGllbnRfdmVyc2lvbiI6IjE3NS4wIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiZGV2aWNlX3ZlbmRvcl9pZCI6Ik5PX0lEXzRfVV9CT1pPIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiIiwiYnJvd3Nlcl92ZXJzaW9uIjoiIiwib3NfdmVyc2lvbiI6IjE2LjAiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo0MzgwMCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==="}
	voicefile = file_content
	filesize = con_len
	rbody = {"files": [{"file_size": filesize, "filename": "voice-message.ogg", "id": "69"}]}
	firstreq = json.loads(requests.post(f'https://discord.com/api/v9/channels/{ctx.channel.id}/attachments', headers=headersforthisshit, json=rbody).text)
	uploadname = firstreq['attachments'][0]["upload_filename"]
	uploadurl = firstreq['attachments'][0]["upload_url"]
	#print(uploadurl)
	#print(uploadname)
	uploadhead = {"Host":"discord-attachments-uploads-prd.storage.googleapis.com","Accept-Language":"en-NZ,en-AU;q=0.9,en;q=0.8","User-Agent":"Discord/42954 CFNetwork/1390 Darwin/22.0.0","Content-Type":"audio/ogg","Connection":"keep-alive","Content-Length":str(filesize)}
	r = requests.put(uploadurl, data=voicefile, headers=uploadhead)
	msgdata = {"channel_id": ctx.channel.id, "flags": 8192, "content": "", "nonce": "", "type": 0, "attachments": [{"id": "0", "filename": "voice-message.ogg", "uploaded_filename": uploadname, "duration_secs": 300.1111111111111111, "waveform": ""}]}
	finallysendthemessage = requests.post(f'https://discord.com/api/v9/channels/{ctx.channel.id}/messages', headers = headersforthisshit, json=msgdata)
