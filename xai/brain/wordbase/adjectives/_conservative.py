

#calss header
class _CONSERVATIVE():
	def __init__(self,): 
		self.name = "CONSERVATIVE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
