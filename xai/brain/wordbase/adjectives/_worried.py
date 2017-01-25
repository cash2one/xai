

#calss header
class _WORRIED():
	def __init__(self,): 
		self.name = "WORRIED"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
