

#calss header
class _NOWHERE():
	def __init__(self,): 
		self.name = "NOWHERE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
