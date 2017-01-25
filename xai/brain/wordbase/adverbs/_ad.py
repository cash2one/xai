

#calss header
class _AD():
	def __init__(self,): 
		self.name = "AD"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
