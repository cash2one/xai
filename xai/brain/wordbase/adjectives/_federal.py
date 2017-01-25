

#calss header
class _FEDERAL():
	def __init__(self,): 
		self.name = "FEDERAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
