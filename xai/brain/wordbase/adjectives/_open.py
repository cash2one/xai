

#calss header
class _OPEN():
	def __init__(self,): 
		self.name = "OPEN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
