

#calss header
class _PREVIOUSLY():
	def __init__(self,): 
		self.name = "PREVIOUSLY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata