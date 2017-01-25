

#calss header
class _ON():
	def __init__(self,): 
		self.name = "ON"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
