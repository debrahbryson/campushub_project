from fastapi import WebSocket

connections = []

async def chat(ws: WebSocket):
	await ws.accept()
	connections.append(ws)
	try:
		while True:
			msg = await ws.receive_text()
		for c in connections:
			await c.send_text(msg)
	except:
		connections.remove(ws)

