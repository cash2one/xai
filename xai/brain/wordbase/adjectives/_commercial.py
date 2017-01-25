

#calss header
class _COMMERCIAL():
	def __init__(self,): 
		self.name = "COMMERCIAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
