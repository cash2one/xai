

#calss header
class _OVER():
	def __init__(self,): 
		self.name = "OVER"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
