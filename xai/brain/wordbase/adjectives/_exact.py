

#calss header
class _EXACT():
	def __init__(self,): 
		self.name = "EXACT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
