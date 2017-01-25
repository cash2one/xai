

#calss header
class _SOUTH():
	def __init__(self,): 
		self.name = "SOUTH"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
