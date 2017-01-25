

#calss header
class _WOOD():
	def __init__(self,): 
		self.name = "WOOD"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
