

#calss header
class _AWAY():
	def __init__(self,): 
		self.name = "AWAY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
