

#calss header
class _DETAILED():
	def __init__(self,): 
		self.name = "DETAILED"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
