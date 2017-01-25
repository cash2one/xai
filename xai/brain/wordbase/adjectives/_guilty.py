

#calss header
class _GUILTY():
	def __init__(self,): 
		self.name = "GUILTY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
