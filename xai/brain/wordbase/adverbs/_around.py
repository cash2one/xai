

#calss header
class _AROUND():
	def __init__(self,): 
		self.name = "AROUND"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
