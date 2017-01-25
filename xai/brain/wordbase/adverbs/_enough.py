

#calss header
class _ENOUGH():
	def __init__(self,): 
		self.name = "ENOUGH"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
