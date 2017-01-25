

#calss header
class _COUNTER():
	def __init__(self,): 
		self.name = "COUNTER"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
