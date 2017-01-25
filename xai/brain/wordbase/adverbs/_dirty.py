

#calss header
class _DIRTY():
	def __init__(self,): 
		self.name = "DIRTY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
