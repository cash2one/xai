

#calss header
class _OUTSIDE():
	def __init__(self,): 
		self.name = "OUTSIDE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata