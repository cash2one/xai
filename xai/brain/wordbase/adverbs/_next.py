

#calss header
class _NEXT():
	def __init__(self,): 
		self.name = "NEXT"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
