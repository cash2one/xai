

#calss header
class _BACK():
	def __init__(self,): 
		self.name = "BACK"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata