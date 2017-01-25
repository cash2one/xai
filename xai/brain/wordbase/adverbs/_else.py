

#calss header
class _ELSE():
	def __init__(self,): 
		self.name = "ELSE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
