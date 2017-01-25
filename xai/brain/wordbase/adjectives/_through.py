

#calss header
class _THROUGH():
	def __init__(self,): 
		self.name = "THROUGH"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
