

#calss header
class _LITTLE():
	def __init__(self,): 
		self.name = "LITTLE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata