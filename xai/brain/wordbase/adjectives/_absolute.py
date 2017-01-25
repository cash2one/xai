

#calss header
class _ABSOLUTE():
	def __init__(self,): 
		self.name = "ABSOLUTE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
