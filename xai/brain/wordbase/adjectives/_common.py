

#calss header
class _COMMON():
	def __init__(self,): 
		self.name = "COMMON"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
