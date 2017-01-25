

#calss header
class _CHINESE():
	def __init__(self,): 
		self.name = "CHINESE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
