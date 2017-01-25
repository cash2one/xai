

#calss header
class _ALWAYS():
	def __init__(self,): 
		self.name = "ALWAYS"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
