

#calss header
class _WIDE():
	def __init__(self,): 
		self.name = "WIDE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
