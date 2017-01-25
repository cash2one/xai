

#calss header
class _FRONT():
	def __init__(self,): 
		self.name = "FRONT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
