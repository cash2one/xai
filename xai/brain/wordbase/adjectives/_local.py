

#calss header
class _LOCAL():
	def __init__(self,): 
		self.name = "LOCAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
