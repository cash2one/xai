

#calss header
class _SPECIFIC():
	def __init__(self,): 
		self.name = "SPECIFIC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
