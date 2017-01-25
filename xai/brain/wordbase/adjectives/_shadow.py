

#calss header
class _SHADOW():
	def __init__(self,): 
		self.name = "SHADOW"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
