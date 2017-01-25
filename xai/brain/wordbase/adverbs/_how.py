

#calss header
class _HOW():
	def __init__(self,): 
		self.name = "HOW"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
