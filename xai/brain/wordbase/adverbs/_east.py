

#calss header
class _EAST():
	def __init__(self,): 
		self.name = "EAST"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
