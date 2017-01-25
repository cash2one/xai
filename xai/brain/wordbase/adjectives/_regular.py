

#calss header
class _REGULAR():
	def __init__(self,): 
		self.name = "REGULAR"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
