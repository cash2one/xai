

#calss header
class _THICK():
	def __init__(self,): 
		self.name = "THICK"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
