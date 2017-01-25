

#calss header
class _BUSY():
	def __init__(self,): 
		self.name = "BUSY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
