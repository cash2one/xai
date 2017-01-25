

#calss header
class _CLASSIC():
	def __init__(self,): 
		self.name = "CLASSIC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
