

#calss header
class _DAILY():
	def __init__(self,): 
		self.name = "DAILY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
