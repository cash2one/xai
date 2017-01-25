

#calss header
class _EVEN():
	def __init__(self,): 
		self.name = "EVEN"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
