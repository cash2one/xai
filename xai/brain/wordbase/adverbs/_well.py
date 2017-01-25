

#calss header
class _WELL():
	def __init__(self,): 
		self.name = "WELL"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
