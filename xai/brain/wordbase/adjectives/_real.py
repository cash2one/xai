

#calss header
class _REAL():
	def __init__(self,): 
		self.name = "REAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
