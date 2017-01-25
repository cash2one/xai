

#calss header
class _DOUBLE():
	def __init__(self,): 
		self.name = "DOUBLE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
