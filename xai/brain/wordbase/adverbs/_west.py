

#calss header
class _WEST():
	def __init__(self,): 
		self.name = "WEST"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
