

#calss header
class _CONCRETE():
	def __init__(self,): 
		self.name = "CONCRETE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
