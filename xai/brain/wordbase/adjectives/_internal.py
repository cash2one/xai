

#calss header
class _INTERNAL():
	def __init__(self,): 
		self.name = "INTERNAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
