

#calss header
class _ILLEGAL():
	def __init__(self,): 
		self.name = "ILLEGAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
