

#calss header
class _FREQUENTLY():
	def __init__(self,): 
		self.name = "FREQUENTLY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
