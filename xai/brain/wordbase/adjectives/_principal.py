

#calss header
class _PRINCIPAL():
	def __init__(self,): 
		self.name = "PRINCIPAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
