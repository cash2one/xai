

#calss header
class _UPPER():
	def __init__(self,): 
		self.name = "UPPER"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
