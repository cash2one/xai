

#calss header
class _ECONOMIC():
	def __init__(self,): 
		self.name = "ECONOMIC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
