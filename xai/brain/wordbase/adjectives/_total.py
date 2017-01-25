

#calss header
class _TOTAL():
	def __init__(self,): 
		self.name = "TOTAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
