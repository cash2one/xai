

#calss header
class _GLOBAL():
	def __init__(self,): 
		self.name = "GLOBAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
