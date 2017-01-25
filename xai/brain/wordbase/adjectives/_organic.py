

#calss header
class _ORGANIC():
	def __init__(self,): 
		self.name = "ORGANIC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
