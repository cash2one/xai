

#calss header
class _PART():
	def __init__(self,): 
		self.name = "PART"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
