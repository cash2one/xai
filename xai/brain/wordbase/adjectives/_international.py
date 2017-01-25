

#calss header
class _INTERNATIONAL():
	def __init__(self,): 
		self.name = "INTERNATIONAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
