

#calss header
class _CRITICAL():
	def __init__(self,): 
		self.name = "CRITICAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
