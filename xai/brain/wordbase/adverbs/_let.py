

#calss header
class _LET():
	def __init__(self,): 
		self.name = "LET"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
