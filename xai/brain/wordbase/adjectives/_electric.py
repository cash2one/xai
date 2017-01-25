

#calss header
class _ELECTRIC():
	def __init__(self,): 
		self.name = "ELECTRIC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
