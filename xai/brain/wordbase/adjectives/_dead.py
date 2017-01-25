

#calss header
class _DEAD():
	def __init__(self,): 
		self.name = "DEAD"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
