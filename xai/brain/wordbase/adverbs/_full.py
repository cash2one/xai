

#calss header
class _FULL():
	def __init__(self,): 
		self.name = "FULL"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
