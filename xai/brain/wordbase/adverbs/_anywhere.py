

#calss header
class _ANYWHERE():
	def __init__(self,): 
		self.name = "ANYWHERE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
