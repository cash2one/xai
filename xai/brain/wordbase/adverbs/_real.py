

#calss header
class _REAL():
	def __init__(self,): 
		self.name = "REAL"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
