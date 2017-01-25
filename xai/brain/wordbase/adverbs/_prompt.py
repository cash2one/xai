

#calss header
class _PROMPT():
	def __init__(self,): 
		self.name = "PROMPT"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
