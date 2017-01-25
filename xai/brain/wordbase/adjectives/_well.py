

#calss header
class _WELL():
	def __init__(self,): 
		self.name = "WELL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
