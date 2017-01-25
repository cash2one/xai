

#calss header
class _SQUARE():
	def __init__(self,): 
		self.name = "SQUARE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
