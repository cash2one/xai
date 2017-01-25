

#calss header
class _SENSITIVE():
	def __init__(self,): 
		self.name = "SENSITIVE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
