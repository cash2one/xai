

#calss header
class _LATIN():
	def __init__(self,): 
		self.name = "LATIN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
