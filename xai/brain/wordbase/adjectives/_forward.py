

#calss header
class _FORWARD():
	def __init__(self,): 
		self.name = "FORWARD"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
