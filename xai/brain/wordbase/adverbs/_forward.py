

#calss header
class _FORWARD():
	def __init__(self,): 
		self.name = "FORWARD"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
