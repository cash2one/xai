

#calss header
class _VARIABLE():
	def __init__(self,): 
		self.name = "VARIABLE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
