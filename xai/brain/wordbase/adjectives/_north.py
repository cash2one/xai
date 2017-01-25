

#calss header
class _NORTH():
	def __init__(self,): 
		self.name = "NORTH"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
