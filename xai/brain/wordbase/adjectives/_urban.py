

#calss header
class _URBAN():
	def __init__(self,): 
		self.name = "URBAN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
