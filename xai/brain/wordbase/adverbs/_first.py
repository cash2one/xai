

#calss header
class _FIRST():
	def __init__(self,): 
		self.name = "FIRST"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
