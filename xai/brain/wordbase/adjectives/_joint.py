

#calss header
class _JOINT():
	def __init__(self,): 
		self.name = "JOINT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
