

#calss header
class _EMPTY():
	def __init__(self,): 
		self.name = "EMPTY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
