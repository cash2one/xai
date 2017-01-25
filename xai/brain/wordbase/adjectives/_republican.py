

#calss header
class _REPUBLICAN():
	def __init__(self,): 
		self.name = "REPUBLICAN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
