

#calss header
class _LIKE():
	def __init__(self,): 
		self.name = "LIKE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata