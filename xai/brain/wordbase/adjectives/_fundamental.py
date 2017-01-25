

#calss header
class _FUNDAMENTAL():
	def __init__(self,): 
		self.name = "FUNDAMENTAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
