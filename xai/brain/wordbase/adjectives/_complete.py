

#calss header
class _COMPLETE():
	def __init__(self,): 
		self.name = "COMPLETE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
