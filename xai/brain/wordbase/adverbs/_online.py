

#calss header
class _ONLINE():
	def __init__(self,): 
		self.name = "ONLINE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
