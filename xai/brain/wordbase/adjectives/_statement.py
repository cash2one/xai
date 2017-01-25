

#calss header
class _STATEMENT():
	def __init__(self,): 
		self.name = "STATEMENT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
