

#calss header
class _VISIBLE():
	def __init__(self,): 
		self.name = "VISIBLE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
