

#calss header
class _BLUE():
	def __init__(self,): 
		self.name = "BLUE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
