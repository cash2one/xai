

#calss header
class _BIOLOGICAL():
	def __init__(self,): 
		self.name = "BIOLOGICAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
