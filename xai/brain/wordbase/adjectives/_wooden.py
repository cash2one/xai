

#calss header
class _WOODEN():
	def __init__(self,): 
		self.name = "WOODEN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
