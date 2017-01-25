

#calss header
class _INITIALLY():
	def __init__(self,): 
		self.name = "INITIALLY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
