

#calss header
class _HIGH():
	def __init__(self,): 
		self.name = "HIGH"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
