

#calss header
class _LONG():
	def __init__(self,): 
		self.name = "LONG"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
