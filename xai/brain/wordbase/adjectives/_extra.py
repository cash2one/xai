

#calss header
class _EXTRA():
	def __init__(self,): 
		self.name = "EXTRA"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
