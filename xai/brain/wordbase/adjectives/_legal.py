

#calss header
class _LEGAL():
	def __init__(self,): 
		self.name = "LEGAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
