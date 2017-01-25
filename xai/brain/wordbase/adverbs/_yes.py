

#calss header
class _YES():
	def __init__(self,): 
		self.name = "YES"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
