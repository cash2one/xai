

#calss header
class _DOUBLE():
	def __init__(self,): 
		self.name = "DOUBLE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
