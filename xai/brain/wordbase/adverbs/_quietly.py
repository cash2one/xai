

#calss header
class _QUIETLY():
	def __init__(self,): 
		self.name = "QUIETLY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
