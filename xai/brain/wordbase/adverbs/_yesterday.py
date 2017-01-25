

#calss header
class _YESTERDAY():
	def __init__(self,): 
		self.name = "YESTERDAY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
