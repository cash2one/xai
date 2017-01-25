

#calss header
class _QUIET():
	def __init__(self,): 
		self.name = "QUIET"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
