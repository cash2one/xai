

#calss header
class _REMAINING():
	def __init__(self,): 
		self.name = "REMAINING"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
