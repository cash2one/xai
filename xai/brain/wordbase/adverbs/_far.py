

#calss header
class _FAR():
	def __init__(self,): 
		self.name = "FAR"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
