

#calss header
class _OFFENSIVE():
	def __init__(self,): 
		self.name = "OFFENSIVE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
