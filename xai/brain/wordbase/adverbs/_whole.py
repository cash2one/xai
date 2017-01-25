

#calss header
class _WHOLE():
	def __init__(self,): 
		self.name = "WHOLE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
