

#calss header
class _INSIDE():
	def __init__(self,): 
		self.name = "INSIDE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata