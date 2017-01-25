

#calss header
class _ARTISTIC():
	def __init__(self,): 
		self.name = "ARTISTIC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
