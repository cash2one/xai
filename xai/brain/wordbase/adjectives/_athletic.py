

#calss header
class _ATHLETIC():
	def __init__(self,): 
		self.name = "ATHLETIC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
