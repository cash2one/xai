

#calss header
class _EITHER():
	def __init__(self,): 
		self.name = "EITHER"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
