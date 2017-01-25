

#calss header
class _AVAILABLE():
	def __init__(self,): 
		self.name = "AVAILABLE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
