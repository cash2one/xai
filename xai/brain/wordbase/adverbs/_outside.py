

#calss header
class _OUTSIDE():
	def __init__(self,): 
		self.name = "OUTSIDE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
