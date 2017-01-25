

#calss header
class _UNIFORM():
	def __init__(self,): 
		self.name = "UNIFORM"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
