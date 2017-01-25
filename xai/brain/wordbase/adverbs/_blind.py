

#calss header
class _BLIND():
	def __init__(self,): 
		self.name = "BLIND"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
