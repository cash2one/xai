

#calss header
class _GOOD():
	def __init__(self,): 
		self.name = "GOOD"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
