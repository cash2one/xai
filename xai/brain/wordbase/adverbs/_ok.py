

#calss header
class _OK():
	def __init__(self,): 
		self.name = "OK"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
