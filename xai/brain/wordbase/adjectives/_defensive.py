

#calss header
class _DEFENSIVE():
	def __init__(self,): 
		self.name = "DEFENSIVE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
