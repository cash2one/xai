

#calss header
class _LATER():
	def __init__(self,): 
		self.name = "LATER"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
