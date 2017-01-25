

#calss header
class _ROUTINE():
	def __init__(self,): 
		self.name = "ROUTINE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
