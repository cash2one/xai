

#calss header
class _CLEAN():
	def __init__(self,): 
		self.name = "CLEAN"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
