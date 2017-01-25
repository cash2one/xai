

#calss header
class _SMALL():
	def __init__(self,): 
		self.name = "SMALL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
