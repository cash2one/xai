

#calss header
class _CIVIL():
	def __init__(self,): 
		self.name = "CIVIL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
