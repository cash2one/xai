

#calss header
class _ANNUAL():
	def __init__(self,): 
		self.name = "ANNUAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
