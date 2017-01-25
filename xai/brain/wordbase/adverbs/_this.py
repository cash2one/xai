

#calss header
class _THIS():
	def __init__(self,): 
		self.name = "THIS"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
