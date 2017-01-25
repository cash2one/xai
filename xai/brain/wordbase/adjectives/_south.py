

#calss header
class _SOUTH():
	def __init__(self,): 
		self.name = "SOUTH"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
