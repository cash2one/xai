

#calss header
class _ASIDE():
	def __init__(self,): 
		self.name = "ASIDE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
