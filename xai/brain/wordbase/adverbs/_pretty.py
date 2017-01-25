

#calss header
class _PRETTY():
	def __init__(self,): 
		self.name = "PRETTY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
