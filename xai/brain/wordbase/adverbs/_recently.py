

#calss header
class _RECENTLY():
	def __init__(self,): 
		self.name = "RECENTLY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
