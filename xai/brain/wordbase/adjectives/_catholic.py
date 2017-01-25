

#calss header
class _CATHOLIC():
	def __init__(self,): 
		self.name = "CATHOLIC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
