

#calss header
class _NEARBY():
	def __init__(self,): 
		self.name = "NEARBY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
