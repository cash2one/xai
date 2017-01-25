

#calss header
class _OBJECTIVE():
	def __init__(self,): 
		self.name = "OBJECTIVE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
