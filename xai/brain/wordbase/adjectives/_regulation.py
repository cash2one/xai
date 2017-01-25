

#calss header
class _REGULATION():
	def __init__(self,): 
		self.name = "REGULATION"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
