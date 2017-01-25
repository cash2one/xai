

#calss header
class _COLLECT():
	def __init__(self,): 
		self.name = "COLLECT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
