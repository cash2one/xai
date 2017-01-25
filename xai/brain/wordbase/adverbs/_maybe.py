

#calss header
class _MAYBE():
	def __init__(self,): 
		self.name = "MAYBE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
