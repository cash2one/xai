

#calss header
class _SPANISH():
	def __init__(self,): 
		self.name = "SPANISH"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
