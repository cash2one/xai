

#calss header
class _BRIEFLY():
	def __init__(self,): 
		self.name = "BRIEFLY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata