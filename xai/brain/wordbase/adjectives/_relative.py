

#calss header
class _RELATIVE():
	def __init__(self,): 
		self.name = "RELATIVE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
