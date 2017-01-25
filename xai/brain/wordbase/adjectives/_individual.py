

#calss header
class _INDIVIDUAL():
	def __init__(self,): 
		self.name = "INDIVIDUAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
