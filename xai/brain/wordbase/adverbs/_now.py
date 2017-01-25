

#calss header
class _NOW():
	def __init__(self,): 
		self.name = "NOW"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
