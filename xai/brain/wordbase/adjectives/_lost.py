

#calss header
class _LOST():
	def __init__(self,): 
		self.name = "LOST"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
