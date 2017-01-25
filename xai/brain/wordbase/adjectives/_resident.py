

#calss header
class _RESIDENT():
	def __init__(self,): 
		self.name = "RESIDENT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
