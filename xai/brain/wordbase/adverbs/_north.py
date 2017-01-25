

#calss header
class _NORTH():
	def __init__(self,): 
		self.name = "NORTH"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
