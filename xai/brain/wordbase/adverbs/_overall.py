

#calss header
class _OVERALL():
	def __init__(self,): 
		self.name = "OVERALL"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
