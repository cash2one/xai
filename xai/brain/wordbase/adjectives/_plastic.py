

#calss header
class _PLASTIC():
	def __init__(self,): 
		self.name = "PLASTIC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
